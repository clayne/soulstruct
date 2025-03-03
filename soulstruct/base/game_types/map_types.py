from __future__ import annotations

__all__ = [
    "Map",

    "MapEntry",
    "MapEntity",

    "MapModel",
    "MapPieceModel",
    "ObjectModel",
    "AssetModel",
    "CharacterModel",
    "PlayerModel",
    "CollisionModel",
    "NavmeshModel",

    "MapEvent",
    "LightEvent",
    "SoundEvent",
    "VFXEvent",
    "WindEvent",
    "TreasureEvent",
    "SpawnerEvent",
    "MessageEvent",
    "ObjActEvent",
    "SpawnPointEvent",
    "MapOffsetEvent",
    "NavigationEvent",
    "EnvironmentEvent",
    "NPCInvasionEvent",

    "Region",

    "MapPart",
    "MapPiece",
    "Object",
    "Asset",
    "Character",
    "Collision",
    "PlayerStart",
    "Navmesh",
    "DummyObject",
    "DummyAsset",
    "DummyCharacter",
    "ConnectCollision",

    "MapTyping",
    "RegionTyping",
    "MapPartTyping",
    "MapPieceTyping",
    "ObjectTyping",
    "AssetTyping",
    "CharacterTyping",
    "CollisionTyping",
    "AnimatedEntityTyping",
    "CoordEntityTyping",
    "SoundEventTyping",
    "NavigationEventTyping",
    "EnvironmentEventTyping",
    "VFXEventTyping",
    "NPCInvasionEventTyping",
]

import typing as tp
from dataclasses import dataclass, field
from enum import unique

from .basic_types import GameObject, GameObjectInt


@dataclass(slots=True)
class Map(GameObject):
    """Represents a game map with associated naming information. Used as an argument in EVS instructions.

    Soulstruct defines constants for existing game maps already, so you shouldn't need to use this class yourself.
    (You can theoretically use transient `Map(a, b)` calls as arguments in EVS instructions, but you may as well
    just use a tuple `(a, b)` in that case, which is also accepted.)

    Args:
        area_id: Area ID of map, which is the first number (of four) in the full map ID. Multiple maps can appear in
            the same area. Some game files (such as lighting parameters) are area-specific rather than map-specific.
        block_id: Block ID of map, which is the second number (of four) in the full map ID. Generally, the area ID
            and block ID fully specify the map. The third number in the map ID is essentially never used and the
            fourth number is only used for file revision purposes (e.g. the Dark Souls DLC version of Darkroot).
        cc_id: Third part of map ID, used only in later games with lots of maps.
        dd_id: Fourth and final part of map ID, used only in later games with lots of maps.

        name: Canonical name of map (e.g. "undeadburg"). Note that the map-finding utility `get_map` ignores case
            and underscores when looking for a specific name.
        variable_name: Name to use in EVS output (typically upper case with underscores).
        verbose_name: Full descriptive name of map for display in certain output-only fields.

        emevd_file_stem: Name of `emevd` file for this map, without extension.
        msb_file_stem: Name of `msb` file for this map, without extension.
        ai_file_stem: Name of 'luabnd[.dcx]' for this map, without extension(s).
        esd_file_stem: Name of 'talkesdbnd[.dcx]' for this map, without extension(s).
    """

    # Four parts of map identifier. May be set to `None` to represent 'maps' that only have specific files, e.g. Common.
    area_id: int | None
    block_id: int | None
    cc_id: int | None = 0
    dd_id: int | None = 0

    name: str = ""  # e.g. "FirelinkShrine"
    verbose_name: str = ""  # e.g. "Firelink Shrine"
    variable_name: str | None = None  # e.g. `FIRELINK_SHRINE`. Must be given for map to be useable in EVS.

    # True stem of map, e.g. for asset subdirectory in `map`.
    # Auto-generated from area and block IDs or left as `None` for non-asset maps.
    map_stem: str | None = field(default=None, init=False)

    # Stems of related map files. If left as "", they will be auto-set based on the map stem (mAA_BB_CC_DD).
    # If explicitly set to `None`, that indicates that the associated file does not exist.
    emevd_file_stem: str | None = ""
    msb_file_stem: str | None = ""
    ai_file_stem: str | None = ""
    esd_file_stem: str | None = ""

    # Lowest-numbered entity ID (e.g. 1020000 for Firelink Shrine) and event flag (e.g. 11020000 for Firelink Shrine).
    # If left as 0, they will be auto-set based on the map ID. If explicitly set to `None`, they should not be used.
    base_entity_id: int | None = 0
    base_flag: int | None = 0

    def __post_init__(self):
        if self.area_id is not None and self.block_id is not None:
            cc_id = self.cc_id or 0
            dd_id = self.dd_id or 0
            self.map_stem = f"m{self.area_id:02d}_{self.block_id:02d}_{cc_id:02d}_{dd_id:02d}"

            # We can set defaults for base entity ID and base flag from area and block IDs.
            if self.base_entity_id == 0:
                self.base_entity_id = 100000 * self.area_id + 10000 * self.block_id
            if self.base_flag == 0:
                self.base_flag = 1000 + 10 * self.area_id + self.block_id
        else:
            self.map_stem = None

        if not self.name:
            if self.map_stem is None:
                raise ValueError("Map must have an area ID and block ID to auto-set `name` from its map stem.")
            self.name = self.map_stem
        # `variable_name` must be set for map to be used in EVS. It has no default string value.
        if not self.verbose_name:
            self.verbose_name = self.name

        for stem in ("emevd", "msb", "ai", "esd"):
            if getattr(self, f"{stem}_file_stem") == "":
                setattr(self, f"{stem}_file_stem", self.map_stem)

        if self.area_id is not None:
            self.base_entity_id = 100000 * self.area_id + 10000 * self.block_id
            self.flag_prefix = 1000 + 10 * self.area_id + self.block_id

    def stem_set(self):
        return {
            stem
            for stem in (self.emevd_file_stem, self.msb_file_stem, self.ai_file_stem, self.esd_file_stem)
            if stem
        }

    def get_connected_map_id(self) -> tuple[int, int, int, int]:
        """Return a tuple with -1 wild cards in place of CC and DD if they are `None`.

        Suitable for use in the `connected_map_id` field of `MSBConnectCollision` instances (as a list).
        """
        if self.area_id is None or self.block_id is None:
            raise ValueError("Cannot get connect tuple for a map with no area ID and/or block ID.")
        cc_id = -1 if self.cc_id is None else self.cc_id
        dd_id = -1 if self.dd_id is None else self.dd_id
        return self.area_id, self.block_id, cc_id, dd_id

    def __hash__(self):
        """Map is uniquely defined by its MSB stem."""
        return hash(self.msb_file_stem)

    def __eq__(self, other_map: Map):
        return self.area_id == other_map.area_id and self.block_id == other_map.block_id

    def __iter__(self):
        return iter((self.area_id, self.block_id, self.cc_id, self.dd_id))

    def __repr__(self):
        return self.emevd_file_stem

    def __getitem__(self, index: int):
        if index == 0:
            return self.area_id
        elif index == 1:
            return self.block_id
        elif index == 2:
            return self.cc_id
        elif index == 3:
            return self.dd_id
        else:
            raise ValueError(f"Index for `Map` must be 0, 1, 2, or 3, not {index}.")

    @classmethod
    def NO_MAP(cls):
        """Used as a default null map in MSB."""
        return cls(0, 0, 0, 0, name="NONE")


class MapEntry(GameObject):
    """Anything that appears in an MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False) -> tuple[str, str | None]:
        """Returns the pluralized name of the MSB type (e.g. "Parts") and the non-pluralized name of the subtype
        (e.g. "Character") or `None` if this is a supertype."""
        raise NotImplementedError


@unique
class MapEntity(MapEntry, GameObjectInt):
    """Any MSB entry with an entity ID (enum values)."""


# region MODELS
class MapModel(MapEntry, GameObjectInt):
    """3D model ID of something."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return "Models", None


class MapPieceModel(MapModel):
    """Map piece model (e.g. m0000)."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Models", "MapPieceModels") if pluralized_subtype else ("Models", "MapPieceModel")


class ObjectModel(MapModel):
    """Object model (e.g. o0000). Only used prior to Elden Ring."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Models", "ObjectModels") if pluralized_subtype else ("Models", "ObjectModel")


class AssetModel(MapModel):
    """Asset model (e.g. AEG123_456). Used in Elden Ring onward."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Models", "AssetModels") if pluralized_subtype else ("Models", "AssetModel")


class CharacterModel(MapModel):
    """Character model (e.g. c0000).

    Note that c0000 can appear in either the Characters or Players parts list in an MSB.
    """
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Models", "CharacterModels") if pluralized_subtype else ("Models", "CharacterModel")


class PlayerModel(MapModel):
    """Sometimes c0000 is registered as this type instead of a CharacterModel."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Models", "PlayerModels") if pluralized_subtype else ("Models", "PlayerModel")


class CollisionModel(MapModel):
    """Collision model (e.g. h0000)."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Models", "CollisionModels") if pluralized_subtype else ("Models", "CollisionModel")


class NavmeshModel(MapModel):
    """Navmesh model (e.g. n0000)."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Models", "NavmesheModels") if pluralized_subtype else ("Models", "NavmeshModel")
# endregion


# region EVENTS
class MapEvent(MapEntity):
    """Base class for things that appear in the 'events' section of the MSB, such as sounds, ObjActs, and VFX."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return "Events", None

    def auto_region_name(self):
        event_enum_subclass = self.__class__.__bases__[0]
        while event_enum_subclass.__bases__[0] is not MapEvent:
            event_enum_subclass = event_enum_subclass.__bases__[0]
        return f"_{event_enum_subclass.__name__}_{self.name.lstrip('_')}"


class LightEvent(MapEvent):
    """Light event in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Lights") if pluralized_subtype else ("Events", "Light")


class SoundEvent(MapEvent):
    """Sound event in MSB attached to a Region (a 'map sound'), which can be enabled or disabled.

    Note that these are enabled on map load, so you may want to disable it (e.g. boss music) in your constructor event.
    """

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Sounds") if pluralized_subtype else ("Events", "Sound")


class VFXEvent(MapEvent):
    """VFX event (visual effect, e.g. fog gate) in MSB attached to a region.

    Can be created or deleted. When deleted, the particles already emitted can be allowed to live out their remaining
    life (`erase_root_only=True` by default).
    """
    @classmethod
    def get_event_arg_fmt(cls):
        return "i"

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "VFX") if pluralized_subtype else ("Events", "VFX")


class WindEvent(MapEvent):
    """Wind event in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Wind") if pluralized_subtype else ("Events", "Wind")


class TreasureEvent(MapEvent):
    """Treasure event in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Treasure") if pluralized_subtype else ("Events", "Treasure")


class SpawnerEvent(MapEvent):
    """Spawner event (causes linked enemies to respawn) in MSB attached to a region. Can be enabled or disabled."""
    @classmethod
    def get_event_arg_fmt(cls) -> str:
        return "i"

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Spawners") if pluralized_subtype else ("Events", "Spawner")


class MessageEvent(MapEvent):
    """Message event in MSB that causes a "developer message" to appear in a region. Can be enabled or disabled."""

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Messages") if pluralized_subtype else ("Events", "Message")


class ObjActEvent(MapEvent):
    """ObjAct (object activation event) added in MSB.

    It can be used in conditions as a test for the ObjAct event being triggered.
    """
    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "ObjActs") if pluralized_subtype else ("Events", "ObjAct")

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        raise TypeError("`ObjActEvent` does not use normal entity IDs, but uses special flags instead.")


class SpawnPointEvent(MapEvent):
    """Spawn point attached to an MSB region."""

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "SpawnPoints") if pluralized_subtype else ("Events", "SpawnPoint")


class MapOffsetEvent(MapEvent):
    """Map offset event in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "MapOffsets") if pluralized_subtype else ("Events", "MapOffset")


class NavigationEvent(MapEvent):
    """Event attached to an MSB navmesh part.

    Enable/disable/toggle functions require you to specify a navigation type; only the flags for that type will be
    modified in the navmesh.
    """
    @classmethod
    def get_event_arg_fmt(cls) -> str:
        return "i"

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Navigation") if pluralized_subtype else ("Events", "Navigation")


class EnvironmentEvent(MapEvent):
    """Environment event in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "Environments") if pluralized_subtype else ("Events", "Environment")


class NPCInvasionEvent(MapEvent):
    """Event describing invasion of NPC's world (e.g. Lautrec) in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Events", "NPCInvasion") if pluralized_subtype else ("Events", "NPCInvasion")


# TODO: Event types from later games.

# endregion


# region REGIONS
class Region(MapEntity):
    """Condition upon a region as a shortcut to condition upon the player being inside it (condition only)."""

    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return "Regions", None

# endregion


# region PARTS
class MapPart(MapEntity):
    """Base class for anything that appears in the Parts section of the MSB."""
    @classmethod
    def get_event_arg_fmt(cls):
        return "i"

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return "Parts", None


class MapPiece(MapPart):
    """Map Piece added in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "MapPieces") if pluralized_subtype else ("Parts", "MapPiece")


class Object(MapPart):
    """Condition upon an object as a shortcut to condition upon it *not* being destroyed."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Objects") if pluralized_subtype else ("Parts", "Object")


class Asset(MapPart):
    """Only used in Elden Ring, in place of 'Objects'. Probably functionally identical but renaming to be clear."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Assets") if pluralized_subtype else ("Parts", "Asset")


class Character(MapPart):
    """Condition upon a character as a shortcut to condition upon them being alive."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Characters") if pluralized_subtype else ("Parts", "Character")


class PlayerStart(MapPart):
    """PlayerStart added in MSB. Used as an argument in `Warp` instructions. No additional state."""

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "PlayerStarts") if pluralized_subtype else ("Parts", "PlayerStart")


class Collision(MapPart):
    """Collision added in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Collisions") if pluralized_subtype else ("Parts", "Collision")


class Navmesh(MapPart):
    """Navmesh instance. NavmeshEvents are attached to it and manipulated with EMEVD."""
    @classmethod
    def get_event_arg_fmt(cls):
        return None  # not valid

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "Navmeshes") if pluralized_subtype else ("Parts", "Navmesh")


class DummyObject(Object):
    """Unused (or cutscene-only) object in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "DummyObjects") if pluralized_subtype else ("Parts", "DummyObject")


class DummyAsset(Asset):
    """Unused (or cutscene-only) asset in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "DummyObjects") if pluralized_subtype else ("Parts", "DummyObject")


class DummyCharacter(Character):
    """Unused (or cutscene-only) character in MSB."""
    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "DummyCharacters") if pluralized_subtype else ("Parts", "DummyCharacter")


class ConnectCollision(MapPart):
    """ConnectCollision added in MSB. No additional state."""
    @classmethod
    def get_event_arg_fmt(cls):
        return None  # not valid

    @classmethod
    def get_msb_entry_supertype_subtype(cls, pluralized_subtype=False):
        return ("Parts", "ConnectCollisions") if pluralized_subtype else ("Parts", "ConnectCollision")

# endregion


# region Type Hints
MapTyping = tp.Union[Map, tuple, list]

RegionTyping = tp.Union[Region, int]

MapPartTyping = tp.Union[MapPart, int]
MapPieceTyping = tp.Union[MapPiece, int]
ObjectTyping = tp.Union[Object, int]
AssetTyping = tp.Union[Asset, int]
CharacterTyping = tp.Union[Character, int]
CollisionTyping = tp.Union[Collision, int]
AnimatedEntityTyping = tp.Union[Object, Character, int]
CoordEntityTyping = tp.Union[Object, Character, Region, int]

LightEventTyping = tp.Union[LightEvent, int]
SoundEventTyping = tp.Union[SoundEvent, int]
NavigationEventTyping = tp.Union[NavigationEvent, int]
EnvironmentEventTyping = tp.Union[EnvironmentEvent, int]
VFXEventTyping = tp.Union[VFXEvent, int]
NPCInvasionEventTyping = tp.Union[NPCInvasionEvent, int]

# endregion
