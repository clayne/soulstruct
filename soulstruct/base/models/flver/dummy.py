from __future__ import annotations

__all__ = ["Dummy"]

from dataclasses import dataclass, field

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.base.models.flver.version import Version


@dataclass(slots=True)
class DummyStruct(BinaryStruct):

    position: Vector3
    _color: list[byte] = field(**BinaryArray(4))  # could be ARGB (Dark Souls 2 only) or BGRA
    forward: Vector3
    reference_id: short
    parent_bone_index: short
    upward: Vector3
    attach_bone_index: short
    flag_1: bool
    use_upward_vector: bool
    unk_x30: int  # only used in Sekiro
    unk_x34: int  # only used in Sekiro
    _pad1: bytes = field(init=False, **BinaryPad(8))


@dataclass(slots=True)
class Dummy:

    position: Vector3
    color_rgba: list[int]  # always stored as RGBA
    forward: Vector3
    reference_id: short
    parent_bone_index: short
    upward: Vector3
    attach_bone_index: short
    flag_1: bool
    use_upward_vector: bool
    unk_x30: int  # only used in Sekiro
    unk_x34: int  # only used in Sekiro

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, flver_version: Version) -> Dummy:
        """For consistency."""
        dummy_struct = DummyStruct.from_bytes(reader)
        _color = dummy_struct.pop("_color")
        color_rgba = list(reversed(_color)) if flver_version == Version.DarkSouls2 else list(_color)
        dummy = dummy_struct.to_object(cls, color_rgba=color_rgba)
        return dummy

    def to_flver_writer(self, writer: BinaryWriter, flver_version: Version):
        _color = tuple(self.color_rgba) if flver_version == Version.DarkSouls2 else tuple(reversed(self.color_rgba))
        dummy_struct = DummyStruct.from_object(self, _color=_color)
        dummy_struct.to_writer(writer)
