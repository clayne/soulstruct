"""Inherits a lot from DS1PTDE."""

__all__ = [
    # EMEVD and EventDirectory classes
    "EMEVD",
    "EventDirectory",
    # Sub-packages / package attributes (contents of constants, instructions, and tests are also in this namespace)
    "constants",
    "enums",
    "decompiler",
    # File utilities
    "convert_events",
    "compare_events",
    # Dark Souls 1 map constants
    "COMMON",
    "DEPTHS",
    "UNDEAD_BURG",
    "FIRELINK_SHRINE",
    "PAINTED_WORLD",
    "DARKROOT_GARDEN",
    "OOLACILE",
    "CATACOMBS",
    "TOMB_OF_THE_GIANTS",
    "ASH_LAKE",
    "BLIGHTTOWN",
    "LOST_IZALITH",
    "SENS_FORTRESS",
    "ANOR_LONDO",
    "NEW_LONDO_RUINS",
    "DUKES_ARCHIVES",
    "KILN_OF_THE_FIRST_FLAME",
    "UNDEAD_ASYLUM",
    # Basic enums
    "OnRestBehavior",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
    "CLIENT_PLAYER_1",
    "CLIENT_PLAYER_2",
    "CLIENT_PLAYER_3",
    "CLIENT_PLAYER_4",
    "CLIENT_PLAYER_5",
    "CLIENT_PLAYER_6",
    "CLIENT_PLAYER_7",
    "CLIENT_PLAYER_8",
    "CLIENT_PLAYER_9",
    # Enums identical in all games
    "AIStatusType",
    "BitOperation",
    "ButtonType",
    "CharacterType",
    "CharacterUpdateRate",
    "ClassType",
    "ComparisonType",
    "CutsceneFlags",
    "DamageTargetType",
    "EventReturnType",
    "FlagType",
    "InterpolationState",
    "ItemType",
    "RangeState",
    "CoordEntityType",
    "NavmeshFlag",
    "NumberButtons",
    "OnOffChange",
    "OnRestBehavior",
    "SoundType",
    "StatueType",
    "SummonSignType",
    "TriggerAttribute",
    "WorldTendencyType",
    "UpdateAuthority",
    # Enums for Dark Souls 1 (both PTD and DSR) only
    "CalculationType",
    "ConditionGroup",
    "Covenant",
    "TeamType",
    "BannerType",
    "MultiplayerState",
    "NPCPartType",
]

from soulstruct.darksouls1ptde.maps import constants
from soulstruct.darksouls1ptde.maps.constants import *
from .emevd import EMEVD, decompiler
from . import enums
from .enums import *
from .event_directory import EventDirectory
from .utilities import convert_events, compare_events
