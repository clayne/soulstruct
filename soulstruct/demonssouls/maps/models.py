from __future__ import annotations

__all__ = [
    "MSBModel",
    "MSBMapPieceModel",
    "MSBObjectModel",
    "MSBCharacterModel",
    "MSBPlayerModel",
    "MSBCollisionModel",
    "MSBNavmeshModel",
    "MSBDummyObjectModel",
    "MSBDummyCharacterModel",
]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.base.maps.msb.models import BaseMSBModel
from soulstruct.utilities.binary import *

from .enums import MSBModelSubtype


class ModelHeaderStruct(MSBHeaderStruct):
    name_offset: int
    _subtype_int: int
    subtype_index: int
    sib_path_offset: int
    instance_count: int
    _pad1: bytes = binary_pad(12, init=False)

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBEntry],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        kwargs = super(ModelHeaderStruct, cls).reader_to_entry_kwargs(reader, entry_type, entry_offset)
        sib_path = reader.unpack_string(
            offset=entry_offset + kwargs.pop("sib_path_offset"), encoding=entry_type.NAME_ENCODING
        )
        kwargs["sib_path"] = sib_path
        kwargs.pop("instance_count")
        return kwargs

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBEntry,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        super(ModelHeaderStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)
        kwargs["sib_path_offset"] = RESERVED
        kwargs.pop("supertype_index")
        if "instance_count" not in kwargs:
            raise ValueError("MSBModel must have `instance_count` set in `kwargs_to_msb_writer`.")

    @classmethod
    def post_write(
        cls,
        entry: MSBModel,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: dict[str, IDList[MSBEntry]],
    ):
        # No super.
        writer.fill("name_offset", writer.position - entry_offset, obj=entry)
        packed_name = entry.name.encode(entry.NAME_ENCODING) + b"\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=entry)
        if entry.sib_path:
            packed_sib_path = entry.sib_path.encode(entry.NAME_ENCODING) + b"\0"
        else:
            packed_sib_path = b"\0\0\0\0\0\0"
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"
        writer.append(packed_sib_path)


@dataclass(slots=True, eq=False, repr=False)
class MSBModel(BaseMSBModel):
    HEADER_STRUCT = ModelHeaderStruct
    NAME_ENCODING = "shift-jis"


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPieceModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.MapPieceModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\sib\\{name}.sib"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)

    def get_model_file_stem(self, map_stem: str):
        """Fix case."""
        return self.name.lower()

    @classmethod
    def model_file_stem_to_model_name(cls, model_stem: str) -> str:
        """Fix case."""
        return model_stem.replace("b", "B")


@dataclass(slots=True, eq=False, repr=False)
class MSBObjectModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.ObjectModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\obj\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacterModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CharacterModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


# UNUSED IN DS1.
# class MSBItemModel(MSBModel):
#     SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.ItemModel


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.PlayerModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCollisionModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CollisionModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\hkxwin\\{name}.hkxwin"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)

    def get_model_file_stem(self, map_stem: str):
        """Fix case."""
        return self.name.lower()

    @classmethod
    def model_file_stem_to_model_name(cls, model_stem: str) -> str:
        """Fix case."""
        return model_stem.replace("b", "B")


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmeshModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.NavmeshModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\navimesh\\{name}.sib"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)

    def get_model_file_stem(self, map_stem: str):
        """Fix case."""
        return self.name.lower()

    @classmethod
    def model_file_stem_to_model_name(cls, model_stem: str) -> str:
        return model_stem.replace("b", "B")


@dataclass(slots=True, eq=False, repr=False)
class MSBDummyObjectModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.DummyObjectModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\obj\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBDummyCharacterModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.DummyCharacterModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\chr\\{name}\\sib\\{name}.sib"
