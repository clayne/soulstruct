from __future__ import annotations

__all__ = ["FLVER"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.containers import Binder, TPF
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Vector4, Matrix3, SINGLE_MIN, SINGLE_MAX
from soulstruct.utilities.misc import IDList

from .bone import FLVERBone
from .dummy import Dummy
from .layout_repair import check_ds1_layouts
from .material import GXItem, write_gx_item_list, Material, Texture
from .submesh import FaceSet, Submesh
from .version import Version
from .vertex_array import VertexArrayHeaderStruct, VertexArrayLayout, VertexArray, VertexDataSizeError

import numpy as np

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class FLVERStruct(BinaryStruct):
    _file_type: bytes = field(init=False, **BinaryString(6, asserted=b"FLVER"))
    endian: bytes = field(**BinaryString(2, asserted=[b"L\0", b"R\0"]))
    version: Version = field(**Binary(int))
    vertex_data_offset: int
    vertex_data_size: int
    dummy_count: int
    material_count: int
    bone_count: int
    mesh_count: int
    vertex_array_count: int
    bounding_box_min: Vector3
    bounding_box_max: Vector3
    true_face_count: int
    total_face_count: int
    face_set_vertex_indices_size: byte = field(**Binary(asserted=[0, 8, 16, 32]))
    unicode: bool
    unk_x4a: bool
    _pad1: bytes = field(init=False, **BinaryPad(1))
    unk_x4c: int
    face_set_count: int
    array_layout_count: int
    texture_count: int
    unk_x5c: byte
    unk_x5d: byte
    _pad2: bytes = field(init=False, **BinaryPad(10))
    unk_x68: int
    _pad3: bytes = field(init=False, **BinaryPad(20))


# noinspection PyDataclass
@dataclass(slots=True)
class FLVER(GameFile):
    """Model format used since Dark Souls PTDE.

    Technically, this format is FLVER2. Demon's Souls used an older version, `FLVER0`, which is not supported here. This
    class supports ALL games from Dark Souls to Elden Ring; minor format differences are handled internally.

    Order of packed binary FLVER information, for reference:
        - FLVER header
        - Material headers
        - Bone headers
        - Submesh headers
        - Submesh face set headers
        - Submesh vertex array headers
        - Vertex array layout headers
        - Array layout types
        - Submesh bounding boxes
        - Submesh bone indices
        - Submesh face set indices
        - Submesh vertex array indices
        - GX item lists
        - Material and texture strings
        - Bone names
        - Vertex data
    """

    EXT: tp.ClassVar = ".flver"
    PATTERN: tp.ClassVar = re.compile(r".*\.flver(\.dcx)?$")

    # Header information that can't be inferred, and must be stored from unpack or manually set. They default to DSR.
    # (These fields have no underscore prefix in `FLVERStruct` and will be passed here automatically.)
    big_endian: bool = False
    version: Version = Version.DarkSouls_A
    bounding_box_min: Vector3 = field(default_factory=Vector3.single_max)
    bounding_box_max: Vector3 = field(default_factory=Vector3.single_min)
    unicode: bool = True
    unk_x4a: bool = False
    unk_x4c: int = 0
    unk_x5c: int = 0
    unk_x5d: int = 0
    unk_x68: int = 0

    dummies: list[Dummy] = field(default_factory=list)
    bones: IDList[FLVERBone] = field(default_factory=IDList)
    submeshes: list[Submesh] = field(default_factory=list)

    # NOTE: `Material` instances are assigned to their submeshes and are not stored separately in the FLVER.
    # On export, all unique materials are packed to the FLVER, and each submesh is assigned an index to one of them.
    
    # NOTE: `GXItem` lists are assigned to the `Material` instances that use them. They are not stored separately in the
    # FLVER. On export, all unique `GXItem` lists are packed to the FLVER, and each `Material` is assigned the offset
    # of its `GXItem` list in the FLVER.

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        byte_order = ByteOrder.from_reader_peek(reader, 2, 6, b"R\0", b"L\0")
        reader.default_byte_order = byte_order  # applies to all FLVER structs
        header = FLVERStruct.from_bytes(reader)
        uv_factor = 2048 if header.version >= Version.DarkSouls2_NT else 1024

        encoding = "utf-16-le" if header.unicode else "shift_jis_2004"

        dummies = [Dummy.from_flver_reader(reader, header.version) for _ in range(header.dummy_count)]

        gx_item_lists = {}  # type: dict[int, list[GXItem]]  # unpacked by each `Material` as encountered
        materials = [
            Material.from_flver_reader(
                reader,
                encoding=encoding,
                version=header.version,
                gx_item_lists=gx_item_lists,
            )
            for _ in range(header.material_count)
        ]

        bones = IDList()  # type: IDList[FLVERBone]
        for _ in range(header.bone_count):
            bone = FLVERBone.from_flver_reader(reader, encoding=encoding)
            bones.append(bone)
        for bone in bones:
            bone.set_bones(bones)

        for bone in bones:
            if id(bone) not in bones._index_dict:
                raise ValueError(f"Bone '{bone.name}' has a duplicate ID in the FLVER bone list?")

        submeshes = [
            Submesh.from_flver_reader(
                reader,
                materials,
                bounding_box_has_unknown=header.version == Version.Sekiro_EldenRing,
            )
            for _ in range(header.mesh_count)
        ]

        face_sets = {
            i: FaceSet.from_flver_reader(
                reader,
                header_vertex_index_size=header.face_set_vertex_indices_size,
                vertex_data_offset=header.vertex_data_offset,
            )
            for i in range(header.face_set_count)
        }

        # Buffer structs come before layouts. We load just the structs first, then combine them with their indexed
        # layout to unpack the vertex array data, which is assigned to submeshes below.
        array_headers = [VertexArrayHeaderStruct.from_bytes(reader) for _ in range(header.vertex_array_count)]

        layouts = [VertexArrayLayout.from_flver_reader(reader) for _ in range(header.array_layout_count)]
        if header.version == Version.DarkSouls_A:
            # Check for botched DS1R array layouts (thanks QLOC!).
            # TODO: At least one DS1R map piece, m0302B0A14, has the correct layout but its data is messed up: there are
            #  16 null bytes at the start of the array (causing the last 16 actual data bytes to be truncated at EOF)
            #  and the Y and Z vertex coordinates are corrupted (appears lossy). Not sure how to handle this beyond a
            #  hard-coded list of DS1R map pieces to fix/warn (currently done in `vertex_array.py` module).
            check_ds1_layouts(layouts, array_headers, submeshes)

        # Load NumPy array wrappers with attached layouts.
        # Uses a dictionary so they can easily be dereferenced to Submeshes.
        vertex_arrays = {}
        for i, array_header in enumerate(array_headers):
            try:
                vertex_array = VertexArray.from_flver_reader(
                    reader, array_header, layouts, header.vertex_data_offset, uv_factor
                )
            except VertexDataSizeError:
                vertex_array = VertexArray(array=np.empty(0), layout=layouts[array_header.layout_index])
            vertex_arrays[i] = vertex_array

        textures = {i: Texture.from_flver_reader(reader, encoding=encoding) for i in range(header.texture_count)}

        # TODO: Sekiro has an additional unknown structure here.

        for material in materials:
            # Each texture is only assigned to ONE material. Texture is popped from `textures` after first assignment.
            material.assign_textures(textures)
        if textures:
            raise ValueError(f"{len(textures)} textures were left over after assignment to materials.")

        for i, submesh in enumerate(submeshes):
            submesh.dereference_face_sets(face_sets)
            submesh.dereference_vertex_arrays(vertex_arrays)
            submesh.validate_unique_data_types()

        if face_sets:
            raise ValueError(f"{len(face_sets)} face sets were left over after assignment to submeshes.")
        if vertex_arrays:
            raise ValueError(f"{len(vertex_arrays)} vertex arrays were left over after assignment to submeshes.")

        return header.to_object(
            cls,
            big_endian=header.endian == b"B\0",
            dummies=dummies,
            bones=bones,
            submeshes=submeshes,
        )

    @classmethod
    def from_path(cls, path: str | Path) -> tp.Self:
        """Reports invalid array layouts."""
        flver = super(FLVER, cls).from_path(path)
        assert isinstance(flver, FLVER)
        if any(mesh.invalid_layout for mesh in flver.submeshes):
            _LOGGER.warning(f"FLVER '{Path(path).name}' has one or more submeshes with invalid vertex array sizes.")
        return flver

    @classmethod
    def from_binder_path(cls, binder_path: str | Path, entry_id_or_name: int | str = None, from_bak=False) -> tp.Self:
        """If not `entry_id_or_name` is given, will search for a lone '.flver{.dcx}' entry in the binder. In this case,
        will raise an exception if no FLVER files or multiple FLVER files exist in the BND.
        """
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)
        if entry_id_or_name is None:
            flver_entry = binder.find_entry_matching_name(r".*\.flver(\.dcx)?$")
            return cls.from_bytes(flver_entry)
        return cls.from_bytes(binder[entry_id_or_name])

    @classmethod
    def multiple_from_binder_path(
        cls, binder_path: Path | str, entry_ids_or_names: tp.Sequence[int | str] = None, from_bak=False
    ) -> list[tp.Self]:
        """If not `entry_ids_or_names` is given, will search for ALL '.flver{.dcx}' entries in the binder and return a
        list of loaded FLVERs. Will raise an exception if no FLVER files are found."""
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)
        if entry_ids_or_names is None:
            flver_entries = binder.find_entries_matching_name(r".*\.flver(\.dcx)?$")
            return [cls.from_bytes(entry) for entry in flver_entries]
        return [cls.from_bytes(binder[entry_id_or_name]) for entry_id_or_name in entry_ids_or_names]

    def to_writer(self) -> BinaryWriter:

        byte_order = ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian
        encoding = byte_order.get_utf_16_encoding() if self.unicode else "shift_jis_2004"

        true_face_count = 0
        total_face_count = 0
        for submesh in self.submeshes:
            allow_primitive_restarts = len(submesh.vertices) < 0xFFFF  # max unsigned short value
            for face_set in submesh.face_sets:
                face_set_true_count, face_set_total_count = face_set.get_face_counts(allow_primitive_restarts)
                true_face_count += face_set_true_count
                total_face_count += face_set_total_count

        if self.version >= Version.Bloodborne_DS3_A:
            # FLVERs from Bloodborne onward: vertex index size is stored per `FaceSet`.
            header_face_set_vertex_indices_size = 0
        else:
            # All `FaceSet`s use the same vertex index size, specified in the FLVER header. We check if all face sets in
            # this FLVER support 16-bit indices. If not, we use 32-bit indices for ALL of them.
            header_face_set_vertex_indices_size = 16
            for submesh in self.submeshes:
                for face_set in submesh.face_sets:
                    if face_set.needs_32bit_indices():
                        _LOGGER.info(f"FLVER '{self.path}' has a face set that requires global 32-bit vertex indices.")
                        header_face_set_vertex_indices_size = 32
                        break
                if header_face_set_vertex_indices_size == 32:
                    break

        header = FLVERStruct.from_object(
            self,
            byte_order=byte_order,
            endian=b"B" if self.big_endian else b"L",
            vertex_data_offset=RESERVED,
            vertex_data_size=RESERVED,
            dummy_count=len(self.dummies),
            material_count=RESERVED,
            bone_count=len(self.bones),
            mesh_count=len(self.submeshes),
            vertex_array_count=sum(len(mesh.vertex_arrays) for mesh in self.submeshes),
            true_face_count=true_face_count,
            total_face_count=total_face_count,
            face_set_vertex_indices_size=header_face_set_vertex_indices_size,  # 0, 16, or 32
            face_set_count=sum(len(mesh.face_sets) for mesh in self.submeshes),
            array_layout_count=RESERVED,
            texture_count=RESERVED,
        )

        writer = header.to_writer(reserve_obj=self)

        for dummy in self.dummies:
            dummy.to_flver_writer(writer, self.version)

        materials_to_pack = []  # type: list[Material]  # unique materials to actually pack to FLVER
        layouts_to_pack = []  # type: list[VertexArrayLayout]  # unique layouts to actually pack to FLVER
        gx_lists_to_pack = []  # type: list[list[GXItem]]  # unique GX item lists to actually pack to FLVER
        hashed_material_indices = {}  # type: dict[int, int]  # maps material hashes to `materials_to_pack` indices
        hashed_layout_indices = {}  # type: dict[int, int]  # maps layout hashes to `layouts_to_pack` indices
        hashed_gx_list_indices = {}  # type: dict[int, int]  # maps GX list hashes to `gx_lists_to_pack` indices
        submesh_material_indices = []  # type: list[int]
        submesh_layout_indices = []  # type: list[list[int]]  # has a list per submesh (may have multiple arrays)
        gx_list_material_users = []  # type: list[list[Material]]  # maps `gx_lists_to_pack` element to `Material` list
        for submesh in self.submeshes:
            material = submesh.material
            material_hash = hash(material)  # includes name!
            if material_hash in hashed_material_indices:
                submesh_material_index = hashed_material_indices[material_hash]
            else:
                # New material.
                submesh_material_index = hashed_material_indices[material_hash] = len(materials_to_pack)
                materials_to_pack.append(material)
                # Check GX item list.
                if material.gx_items:
                    gx_items_hash = hash(tuple(material.gx_items))
                    if gx_items_hash in hashed_gx_list_indices:
                        # GX item list already registered for packing.
                        material_gx_list_index = hashed_gx_list_indices[gx_items_hash]
                        gx_list_material_users[material_gx_list_index].append(material)
                    else:
                        # New GX item list.
                        material_gx_list_index = len(gx_lists_to_pack)
                        hashed_gx_list_indices[gx_items_hash] = material_gx_list_index
                        gx_lists_to_pack.append(material.gx_items)
                        gx_list_material_users.append([material])
            submesh_material_indices.append(submesh_material_index)

            array_layout_indices = []
            for vertex_array in submesh.vertex_arrays:
                layout = vertex_array.layout
                layout_hash = hash(tuple((data_type.type_int, data_type.format_enum) for data_type in layout))
                if layout_hash in hashed_layout_indices:
                    array_layout_index = hashed_layout_indices[layout_hash]
                else:
                    # New layout.
                    array_layout_index = hashed_layout_indices[layout_hash] = len(layouts_to_pack)
                    layouts_to_pack.append(layout)
                array_layout_indices.append(array_layout_index)
            submesh_layout_indices.append(array_layout_indices)

        writer.fill("material_count", len(materials_to_pack), obj=self)
        writer.fill("array_layout_count", len(layouts_to_pack), obj=self)
        writer.fill("texture_count", sum(len(material.textures) for material in materials_to_pack), obj=self)

        # Pack materials.
        for material in materials_to_pack:
            material.to_flver_writer(writer)

        # Pack bones.
        for bone in self.bones:
            bone.set_bone_indices(self.bones)
            bone.to_flver_writer(writer, self.bones)

        # Pack submesh headers.
        for submesh, material_index in zip(self.submeshes, submesh_material_indices):
            submesh.to_flver_writer(writer, material_index)

        # Pack submesh face sets.
        face_set_index_sizes = []
        for submesh in self.submeshes:
            for face_set in submesh.face_sets:
                if header_face_set_vertex_indices_size != 0:
                    # Vertex size set globally in FLVER header, depending on largest face set (older FLVERs).
                    # No value is written to each Face Set.
                    face_set_vertex_index_size = header_face_set_vertex_indices_size
                    write_index_size = False
                else:
                    # Vertex size set per `FaceSet`. These sizes are stored for packing below.
                    face_set_vertex_index_size = 32 if face_set.needs_32bit_indices() else 16
                    write_index_size = True
                face_set_index_sizes.append(face_set_vertex_index_size)  # to save time below
                face_set.to_flver_writer(writer, face_set_vertex_index_size, write_index_size)

        # Pack submesh vertex array headers.
        for submesh, layout_indices in zip(self.submeshes, submesh_layout_indices):
            for i, (vertex_array, layout_index) in enumerate(zip(submesh.vertex_arrays, layout_indices)):
                vertex_array.to_flver_writer(
                    writer,
                    write_array_length=self.version >= 0x20005,
                    layout_index=layout_index,
                    array_index=i,
                )

        # Pack array layouts.
        for layout in layouts_to_pack:
            layout.to_flver_writer(writer)

        # Pack material textures.
        first_texture_index = 0
        for material in materials_to_pack:
            material.pack_textures(writer, first_texture_index=first_texture_index)
            first_texture_index += len(material.textures)

        # TODO: Write unknown Sekiro struct here.

        # Indexed data only after this point, aligning to 16 bytes between each data type.

        writer.pad_align(16)
        for layout in layouts_to_pack:
            layout.pack_layout_types(writer)

        writer.pad_align(16)
        for submesh in self.submeshes:
            submesh.pack_bounding_box(writer)

        writer.pad_align(16)
        bone_indices_start = writer.position
        for submesh in self.submeshes:
            submesh.pack_bone_indices(writer, bone_indices_start=bone_indices_start)

        writer.pad_align(16)
        first_face_set_index = 0
        for submesh in self.submeshes:
            submesh.pack_face_set_indices(writer, first_face_set_index)
            first_face_set_index += len(submesh.face_sets)

        writer.pad_align(16)
        first_vertex_array_index = 0
        for submesh in self.submeshes:
            submesh.pack_vertex_array_indices(writer, first_vertex_array_index)
            first_vertex_array_index += len(submesh.vertex_arrays)

        # Pack GX lists.
        writer.pad_align(16)
        for gx_list, material_users in zip(gx_lists_to_pack, gx_list_material_users):
            gx_list_offset = writer.position
            write_gx_item_list(writer, gx_list)
            for material in material_users:
                # NOTE: Material only reserves this field if it has any GX items. Otherwise, already wrote offset -1.
                material.fill_gx_offset(writer, gx_list_offset)

        # Pack material and texture strings.
        writer.pad_align(16)
        for material in materials_to_pack:
            material.pack_strings(writer, encoding)
            for texture in material.textures:
                texture.pack_strings(writer, encoding=encoding)

        writer.pad_align(16)
        for bone in self.bones:
            bone.pack_name(writer, encoding=encoding)

        alignment = 32 if self.version <= 0x2000E else 16
        writer.pad_align(alignment)
        if self.version in {Version.DarkSouls2_NT, Version.DarkSouls2}:
            writer.pad(32)

        vertex_data_start = writer.position
        writer.fill("vertex_data_offset", vertex_data_start, obj=self)

        face_set_index = 0
        for submesh in self.submeshes:
            for face_set in submesh.face_sets:
                writer.pad_align(16)
                face_set.pack_vertex_indices(
                    writer,
                    vertex_index_size=face_set_index_sizes[face_set_index],
                    vertex_indices_offset=writer.position - vertex_data_start,
                )
                face_set_index += 1

            for vertex_array in submesh.vertex_arrays:
                writer.pad_align(16)
                uv_factor = 2048 if self.version >= Version.DarkSouls2_NT else 1024
                vertex_array.pack_array(
                    writer,
                    array_offset=writer.position - vertex_data_start,
                    uv_factor=uv_factor,
                )

        writer.pad_align(16)
        writer.fill("vertex_data_size", writer.position - vertex_data_start, obj=self)
        if self.version in {Version.DarkSouls2_NT, Version.DarkSouls2}:
            writer.pad(32)

        return writer

    def to_obj(self, name="FLVER", submeshes=()) -> str:
        if isinstance(submeshes, int):
            submeshes = [submeshes]
        vertex_offset = 0
        mesh_objs = []
        for i, mesh in enumerate(self.submeshes):
            if submeshes and i not in submeshes:
                continue  # skip this mesh
            mesh_objs.append(mesh.to_obj(name=f"{name} Submesh {i}", vertex_offset=vertex_offset))
            vertex_offset += len(mesh.vertices)
        return "\n\n".join(mesh_objs)

    def write_obj(self, obj_path: Path | str = None, obj_name="", make_dirs=True, submeshes=()):
        if obj_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            obj_path = self.path
            if obj_path.suffix == ".dcx":
                obj_path = obj_path.with_name(obj_path.stem)
            obj_path = obj_path.with_suffix(".obj")
        else:
            obj_path = Path(obj_path)
            if obj_path.suffix != ".obj":
                obj_path = obj_path.with_suffix(".obj")
        if make_dirs:
            obj_path.parent.mkdir(parents=True, exist_ok=True)
        if not obj_name:
            obj_name = obj_path.stem
        obj_str = self.to_obj(name=obj_name, submeshes=submeshes)
        with obj_path.open("w") as f:
            f.write(obj_str)

    def to_string(self) -> str:
        if self.bones:
            bones = "[\n    " + "\n    ".join(repr(self.bones)[1:-1].split("\n")) + "\n  ]"
        else:
            bones = "[]"
        if self.dummies:
            dummies = "[\n    " + "\n    ".join(repr(self.dummies)[1:-1].split("\n")) + "\n  ]"
        else:
            dummies = "[]"
        if self.submeshes:
            submeshes = "[\n    " + "\n    ".join(repr(self.submeshes)[1:-1].split("\n")) + "\n  ]"
        else:
            submeshes = "[]"
        return (
            f"FLVER(\n"
            f"  bones = {bones}\n"
            f"  dummies = {dummies}\n"
            f"  submeshes = {submeshes}\n"
            ")"
        )

    def __setstate__(self, state: tuple[None, dict[str, tp.Any]]):
        """Dereference bone connections after restoring state."""
        _, slot_dict = state
        for field_name, field_value in slot_dict.items():
            setattr(self, field_name, field_value)
        for bone in self.bones:
            bone.set_bones(self.bones)

    def __repr__(self) -> str:
        return f"FLVER({len(self.submeshes)} submeshes, {len(self.bones)} bones, {len(self.dummies)} dummies)"

    def draw(self, auto_show=False, show_mesh_face_sets=(), show_origin=False, axes=None, **kwargs):
        import matplotlib.pyplot as plt
        if show_mesh_face_sets == "all":
            show_mesh_face_sets = tuple(range(len(self.submeshes)))
        if axes is None:
            axes = plt.figure().add_subplot(111, projection="3d")
        for i, mesh in enumerate(self.submeshes):
            mesh.draw(
                show_origin=show_origin and mesh is self.submeshes[-1],
                show_face_sets=show_mesh_face_sets,
                auto_show=False,
                axes=axes,
                **kwargs,
            )
        for bone in self.bones:
            bone_position, _, _ = bone.get_armature_space_transform()
            axes.scatter(*bone_position.to_xzy(), color="blue", s=10)
        if auto_show:
            plt.show()

    def scale_all_translations(self, scale_factor: float | Vector3 | Vector4):
        """Modifies the FLVER in place by scaling all dummies, bones, and vertex positions by `factor`.

        NOTE: As a reminder, FLVER files are for APPEARANCE ONLY (and dummies for TAE events). You will have to scale
        the corresponding HKX files (map collision, character skeletons/ragdolls, etc.) before gameplay will really be
        affected.
        """
        if isinstance(scale_factor, Vector4):
            scale_factor = Vector3((scale_factor.x, scale_factor.y, scale_factor.z))
        for dummy in self.dummies:
            dummy.translate *= scale_factor
        for bone in self.bones:
            bone.translate *= scale_factor
        if isinstance(scale_factor, (int, float)):
            scale_factor = Vector3((scale_factor, scale_factor, scale_factor))
        for submesh in self.submeshes:
            for vertex_array in submesh.vertex_arrays:
                # Scale all three position columns.
                position = vertex_array["position"]
                # TODO: Should be able to broadcast this in one line.
                position[0] *= scale_factor.x
                position[1] *= scale_factor.y
                position[2] *= scale_factor.z

    # region Materials/Textures

    def replace_tpf_name(self, old_name: str, new_name: str):
        """Iterate over all `Material` textures and replace all '{old_name}.tga' names with '{new_name}.tga'."""
        for submesh in self.submeshes:
            for texture in submesh.material.textures:
                # TODO: To be safe, probably make sure we're only replacing the file name of the path.
                texture.path = texture.path.replace(old_name, new_name)

    def get_all_texture_paths(self) -> set[Path]:
        """Get set of all texture paths from all materials, which typically end in '.tga' or '.tif'.

        Ignores textures with empty `path`.
        """
        return {
            Path(texture.path)
            for submesh in self.submeshes
            for texture in submesh.material.textures if texture.path
        }

    def get_tpfbhd_directory_path(self) -> Path:
        """Looks for folder containing TPFBHD files adjacent to FLVER's directory.

        Only works for map pieces right now, and requires them to be loaded from their native location (e.g.
        `{data}/map/m10_00_00_00`).
        """
        if not self.path:
            raise ValueError(f"Cannot automatically find `tpfbhd` directory (FLVER path is unknown).")
        flver_parent = self.path.parent
        map_directory_match = re.match(r"^(m\d\d)_\d\d_\d\d_\d\d$", flver_parent.name)
        if not map_directory_match:
            raise ValueError(f"FLVER is not located in a map folder (`mAA_BB_CC_DD`).")
        tpfbhd_directory = flver_parent / f"../{map_directory_match.group(1)}"
        if not tpfbhd_directory.is_dir():
            raise FileNotFoundError(f"Required TPFBHD directory does not exist: {tpfbhd_directory}")
        return tpfbhd_directory

    def find_all_tpfs(self, tpfbhd_directory: None | str | Path = None) -> dict[Path, TPF]:
        if tpfbhd_directory is None:
            tpfbhd_directory = self.get_tpfbhd_directory_path()
        else:
            tpfbhd_directory = Path(tpfbhd_directory)
        tpf_paths = [(p, re.compile(rf"{p.stem}\.tpf(\.dcx)?$")) for p in self.get_all_texture_paths()]
        tpf_sources = {}
        for bhd_path in tpfbhd_directory.glob("*.tpfbhd"):
            bxf = Binder.from_path(bhd_path)
            for entry in bxf.entries:
                for tpf_path, tpf_re in reversed(tpf_paths):
                    if tpf_re.match(entry.name):
                        tpf_paths.remove((tpf_path, tpf_re))
                        tpf_sources[tpf_path] = TPF.from_bytes(entry.data)
                        break
                if not tpf_paths:
                    break
            if not tpf_paths:
                break
        return tpf_sources

    # endregion

    # region Bones

    def sort_submesh_bone_indices(self):
        """Sort local `bone_indices` of each submesh, if used."""
        for submesh in self.submeshes:
            submesh.sort_bone_indices()

    def refresh_bone_bounding_boxes(self, in_local_space=True, only_bones: tp.Container[int] = ()):
        """Refresh the bounding box of each bone by finding every vertex in every submesh weighted to it.

        As you'd expect, this is a little expensive, though less so with `NumPy`, thankfully. Optionally allows
        restriction to only certain bones, in case you KNOW which bones need refreshing and don't want to waste time on
        the others.

        Note that rigged FLVERs (characters, objects) seem to always use `in_local_space=True`, while map pieces do not.
        """

        if in_local_space:
            # Get the inverse transforms required to convert each bone's vertex positions to local bone space.
            bone_arma_translate_inv_rotates = [
                (translate, rotate.inverse())
                for translate, rotate, _ in self.get_bone_armature_space_transforms()
            ]
        else:
            # Unused.
            bone_arma_translate_inv_rotates = []

        refresh_bone_indices = [i for i, bone in enumerate(self.bones) if not only_bones or i in only_bones]

        # 3D arrays that track min/max vertex positions for each bone and axis.
        bone_mins = SINGLE_MAX * np.ones((len(self.bones), 3))
        bone_maxs = SINGLE_MIN * np.ones((len(self.bones), 3))

        # We need to check all bone indices in every vertex array in every submesh.
        for submesh in self.submeshes:

            for vertex_array in submesh.vertex_arrays:

                used_bone_vertex_indices = {}  # tracks vertex indices used by each bone

                position = vertex_array["position"]
                bone_indices = vertex_array["bone_indices"]
                if submesh.bone_indices is not None:
                    # Remap bone indices to global indices.
                    bone_indices = submesh.bone_indices[bone_indices]

                try:
                    bone_weights = vertex_array["bone_weights"]
                except ValueError:
                    # No bone weights (map piece 'pose' mode). We only need to look at first bone index (always used).
                    for bone_index in refresh_bone_indices:
                        used_bone_vertex_indices[bone_index] = bone_indices[:, 0] == bone_index
                else:
                    # Only check bone indices where weight is non-zero.
                    for bone_index in refresh_bone_indices:
                        used = ((bone_indices == bone_index) & (bone_weights > 0.0)).any(axis=1)
                        used_bone_vertex_indices[bone_index] = used

                for bone_index, vertex_indices in used_bone_vertex_indices.items():
                    if not np.any(vertex_indices):
                        continue  # bone unused by this submesh array

                    # Get vertex positions for this bone.
                    # TODO: "IndexError: boolean index did not match indexed array along dimension 1; dimension is 3
                    #  but corresponding boolean dimension is 4."
                    bone_vertex_positions = position[vertex_indices]

                    if in_local_space:
                        # Transform vertex positions into bone local space (typical for characters).
                        arma_translate, inv_arma_rotate = bone_arma_translate_inv_rotates[bone_index]
                        bone_vertex_positions -= arma_translate.data
                        bone_vertex_positions = bone_vertex_positions @ inv_arma_rotate.data.T

                    # Get bounds for this vertex array.
                    bone_vertex_mins = np.min(bone_vertex_positions, axis=0)
                    bone_vertex_maxs = np.max(bone_vertex_positions, axis=0)

                    # Update FLVER-wide bounds across all submeshes and vertex arrays.
                    bone_mins[bone_index] = np.min((bone_mins[bone_index], bone_vertex_mins), axis=0)
                    bone_maxs[bone_index] = np.max((bone_maxs[bone_index], bone_vertex_maxs), axis=0)

        # Update bone bounding boxes.
        for bone_index in refresh_bone_indices:
            # print(f"BEFORE: {bone.name}: {bone.bounding_box_min} -> {bone.bounding_box_max}")
            bone = self.bones[bone_index]
            bone.bounding_box_min = Vector3(bone_mins[bone_index])
            bone.bounding_box_max = Vector3(bone_maxs[bone_index])
            # print(f"    --> {bone.name}: {bone.bounding_box_min} -> {bone.bounding_box_max}")

    def refresh_bounding_boxes(self):
        """Refresh global bounding box of FLVER from minimum and maximum positions of all submesh vertices, along with
        the submesh-specific bounding boxes if used.

        TODO: Should probably call this automatically on FLVER write.
        """
        if not self.submeshes:
            # Empty FLVER.
            _LOGGER.warning(f"FLVER '{self.path}' has no submeshes. Setting maximal bounding box.")
            self.bounding_box_min = Vector3((SINGLE_MAX, SINGLE_MAX, SINGLE_MAX))
            self.bounding_box_max = Vector3((SINGLE_MIN, SINGLE_MIN, SINGLE_MIN))
            return

        submesh_mins = np.empty((len(self.submeshes), 3))
        submesh_maxs = np.empty((len(self.submeshes), 3))

        for i, submesh in enumerate(self.submeshes):
            submesh_min = np.array([SINGLE_MAX] * 3)
            submesh_max = np.array([SINGLE_MIN] * 3)
            for vertex_array in submesh.vertex_arrays:
                position = vertex_array["position"]
                submesh_min = np.minimum(submesh_min, position.min(axis=0))
                submesh_max = np.maximum(submesh_max, position.max(axis=0))

            if submesh.uses_bounding_box:
                submesh.bounding_box_min = Vector3(submesh_min)
                submesh.bounding_box_max = Vector3(submesh_max)
                # TODO: Don't know how to set `bounding_box_unknown` in Sekiro+.

            submesh_mins[i, :] = submesh_min
            submesh_maxs[i, :] = submesh_max

        # Update FLVER-wide bounding box.
        self.bounding_box_min = Vector3(submesh_mins.min(axis=0))
        self.bounding_box_max = Vector3(submesh_maxs.max(axis=0))

    def get_root_bones(self) -> list[FLVERBone]:
        """Return all bones with no parent."""
        return [bone for bone in self.bones if bone.parent_bone is None]

    def set_bone_children_siblings(self):
        """Iterate through the `bones` hierarchy and use set `parent_bone` (the most important reference) to set
        `child_bone` (first bone using this bone as parent) and sibling bones (ordered bones with the same parent).
        """

        # Clear old references.
        for bone in self.bones:
            bone.child_bone = None
            bone.previous_sibling_bone = None
            bone.next_sibling_bone = None

        root_bones = []
        for bone in self.bones:

            if bone.parent_bone is None:
                # Root bone. Assign siblings.
                if root_bones:
                    # Next sibling.
                    root_bones[-1].next_sibling_bone = bone
                    bone.previous_sibling_bone = root_bones[-1]
                root_bones.append(bone)

            children = []
            for other_bone in self.bones:
                if other_bone.parent_bone is bone:
                    if not children:
                        # First child found.
                        bone.child_bone = other_bone
                    else:
                        # Next sibling.
                        children[-1].next_sibling_bone = other_bone
                        other_bone.previous_sibling_bone = children[-1]
                    children.append(other_bone)

    def get_bone_armature_space_transforms(self) -> list[tuple[Vector3, Matrix3, Vector3]]:
        """Compute the FLVER armature space transforms of all bones at once by moving downward through the hierarchy.

        Note that bone scale is not inherited. All scale values are local.

        Also note that we can't cache this because any/all parent bone transforms could change. It's inexpensive anyway.
        """
        root_bones = self.get_root_bones()
        # Start with local transforms. They will be changed to armature space transforms one at a time, recursively.
        armature_space_transforms = [bone.get_local_transform() for bone in self.bones]
        done_indices = set()

        def local_to_parent_space(bone: FLVERBone, parent_transform: tuple[Vector3, Matrix3, Vector3]):
            index = bone.get_bone_index(self.bones)
            if index in done_indices:
                raise ValueError(f"Bone '{bone.name}' is a child of multiple bones.")
            done_indices.add(index)
            local_translate, local_rotate_matrix, local_scale = armature_space_transforms[index]
            parent_translate, parent_rotate_matrix, _ = parent_transform
            bone_armature_transform = (
                parent_translate + parent_rotate_matrix @ local_translate,
                parent_rotate_matrix @ local_rotate_matrix,
                local_scale,  # scale not inherited
            )
            armature_space_transforms[index] = bone_armature_transform
            for child_bone in bone.get_all_immediate_children():
                local_to_parent_space(child_bone, bone_armature_transform)

        for root_bone in root_bones:
            local_to_parent_space(root_bone, (Vector3.zero(), Matrix3.identity(), Vector3.one()))

        return armature_space_transforms

    def set_bone_armature_space_transforms(self, armature_space_transforms: list[tuple[Vector3, Matrix3, Vector3]]):
        """Use given `armature_space_transforms` to set the local transforms of each `FLVERBone`, by applying the
        inverse of each parent's armature space transform (conveniently available).

        NOTE: Bone scale is NOT inherited. All scale vectors in `armature_space_transforms` will be treated as local
        bone scale vectors.
        """

        if (arma_count := len(armature_space_transforms)) != len(self.bones):
            raise ValueError(f"Expected {len(self.bones)} armature space transforms, but got {arma_count}.")

        parent_inv_rots = {}  # type: dict[int, Matrix3]

        for bone_index, bone in enumerate(self.bones):
            arma_transform = armature_space_transforms[bone_index]
            parent_bone = bone.parent_bone
            if parent_bone is None:
                # Root bone: armature space transform is local transform.
                bone.set_local_transform(arma_transform)
                continue

            parent_index = parent_bone.get_bone_index(self.bones)

            # Get parent transform and apply inverse to this bone's armature space transform.
            arma_translate, arma_rotate_matrix, arma_scale = arma_transform
            parent_arma_translate, parent_arma_rotate_matrix, _ = armature_space_transforms[parent_index]
            parent_arma_inv_rotate = parent_inv_rots.setdefault(parent_index, parent_arma_rotate_matrix.inverse())

            bone.set_local_transform((
                parent_arma_inv_rotate @ (arma_translate - parent_arma_translate),
                parent_arma_inv_rotate @ arma_rotate_matrix,
                arma_scale,  # scale not inherited
            ))

    def check_if_all_zero_bone_weights(self) -> bool:
        """Reliable (so far) indicator of map piece FLVER, as opposed to character/object FLVER.

        Map pieces sometimes use bone indices as an offset for certain submeshes (or even a subset of a mesh's 
        vertices), but never use bone weights (in DS1 at least).

        This method checks every vertex and is therefore reasonably expensive to compute, so do it sparingly.
        """
        for m in self.submeshes:
            for v in m.vertices:
                if any(v.bone_weights):
                    return False
        return True

    def debone_map_piece(self, default_bone_name="", refresh_bone_bounding_boxes=True):
        """Remove all bones from a Map Piece FLVER by baking the bones into the vertices that use them and setting all
        submeshes and vertices to use only the default bone (index 0).

        Some of From's older map pieces, like Sunlight Altar and Andre's building in DS1 m10_01_00_00, use bones even
        just to place certain walls of buildings, which is extremly weird and annoying for editing. This function bakes
        all bone transforms into the vertices that use them, then removes all bones except the default bone (0), which
        is moved to the origin and named after the FLVER model (standard practice).

        If `default_bone_name` is not given, we will try to get it from the minimal stem of `self.path`. If that fails,
        we will use 'FLVER' and issue a warning.

        NOTE: Not intended for use with map pieces that use bones to place individual trees and shrubs whose mesh data
        is centered at the origin, which is an actual good way to use bones in a Map Piece!
        """
        if any(submesh.is_bind_pose for submesh in self.submeshes):
            raise ValueError("Cannot debone FLVER models with any `is_bind_pose` submeshes (i.e. must be Map Piece).")

        if not default_bone_name:
            if self.path:
                # NOTE: Map Piece default bone names are sometimes FLVER model stems (with 'AXX' suffix, etc.) and
                # sometimes the reduced model name that appears in MSB Map Piece models (without suffix/map). We use
                # the full model name here, since this is going in the model file.
                default_bone_name = self.path_minimal_stem
            else:
                default_bone_name = "FLVER"
                _LOGGER.warning(f"Could not get default bone name from FLVER path. Using bone name 'FLVER'.")

        if len(self.bones) == 1:
            if (
                self.bones[0].translate == Vector3.zero()
                and self.bones[0].rotate == Vector3.zero()
                and self.bones[0].scale == Vector3.one()
            ):
                print(f"FLVER {self.path.name} is already deboned (only has one bone at the origin).")
                return

        bone_transforms = {}
        for i, bone in enumerate(self.bones):
            bone_transforms[i] = (bone.translate, Matrix3.from_euler_angles(bone.rotate, radians=True), bone.scale)

        for submesh in self.submeshes:
            for vertex_array in submesh.vertex_arrays:
                array = vertex_array.array
                local_bone_indices = array["bone_indices"][:, 0]  # only first index needed
                if submesh.bone_indices is not None:
                    global_bone_indices = submesh.bone_indices[local_bone_indices].tolist()
                else:
                    global_bone_indices = local_bone_indices.tolist()
                if len(np.unique(global_bone_indices)) == 1:
                    # All vertices use the same bone. No need to iterate over rows; just transform all positions.
                    t, r, s = bone_transforms[global_bone_indices[0]]
                    # Scale, then rotate, then translate.
                    array["position"] = (s.data * array["position"]) @ r.data.T + t.data
                    for array_field in array.dtype.names:
                        if array_field in ("normal", "bitangent") or array_field.startswith("tangent"):
                            # Just rotate unit vector. Don't bother normalizing; FLVER compression will dwarf errors.
                            array[array_field][:, :3] = array[array_field][:, :3] @ r.data.T
                else:
                    # Multiple bones used. Iterate over rows. TODO: Probably a faster way to do this.
                    for i in range(len(array)):
                        t, r, s = bone_transforms[global_bone_indices[i]]
                        # Scale, then rotate, then translate.
                        array["position"][i] = r.data @ (s.data * array["position"][i]) + t.data
                        for array_field in array.dtype.names:
                            if array_field in ("normal", "bitangent") or array_field.startswith("tangent"):
                                array[array_field][i][:3] = r.data @ array[array_field][i][:3]  # rotating a single row

                # Now set all bone indices to zero.
                array["bone_indices"][:, :] = 0

            if submesh.bone_indices is not None:
                # Set submesh local bones to [0].
                submesh.bone_indices = np.array([0])

        # All bones baked into all submeshes. Remove all but the default bone (0).
        self.bones.clear()
        self.bones.append(FLVERBone(name=default_bone_name))

        if refresh_bone_bounding_boxes:
            self.refresh_bone_bounding_boxes(in_local_space=False)
        self.refresh_bounding_boxes()

    # endregion
