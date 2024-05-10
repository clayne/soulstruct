__all__ = [
    # EMEVD class
    "EMEVD",
    "EventDirectory",
    # Sub-packages / package attributes (contents of constants, instructions, and tests are also in this namespace)
    "constants",
    "enums",
    "decompiler",
    # File utilities
    "compare_events",
    "convert_events",
    # Elden Ring map constants
    "COMMON",
    "COMMON_FUNC",
    "STORMVEIL_CASTLE",
    "CHAPEL_OF_ANTICIPATION",
    "LEYNDELL_ROYAL_CAPITAL",
    "LEYNDELL_ASHEN_CAPITAL",
    "ROUNDTABLE_HOLD",
    "AINSEL_RIVER",
    "SIOFRA_RIVER",
    "DEEPROOT_DEPTHS",
    "ASTEL_ARENA",
    "MOHGWYN_PALACE",
    "SIOFRA_RIVER_START",
    "ANCESTOR_SPIRIT_ARENA",
    "REGAL_ANCESTOR_ARENA",
    "CRUMBLING_FARUM_AZULA",
    "RAYA_LUCARIA",
    "HALIGTREE",
    "VOLCANO_MANOR",
    "STRANDED_GRAVEYARD",
    "STONE_PLATFORM",
    "SHUNNING_GROUNDS",
    "RUIN_STREWN_PRECIPICE",

    # Generic dungeons
    "TOMBSWARD_CATACOMBS",
    "IMPALERS_CATACOMBS",
    "STORMFOOT_CATACOMBS",
    "ROADS_END_CATACOMBS",
    "MURKWATER_CATACOMBS",
    "BLACK_KNIFE_CATACOMBS",
    "CLIFFBOTTOM_CATACOMBS",
    "WYNDHAM_CATACOMBS",
    "SAINTED_HEROS_GRAVE",
    "GELMIR_HEROS_GRAVE",
    "AURIZA_HEROS_GRAVE",
    "DEATHTOUCHED_CATACOMBS",
    "UNSIGHTLY_CATACOMBS",
    "AURIZA_SIDE_TOMB",
    "MINOR_ERDTREE_CATACOMBS",
    "CAELID_CATACOMBS",
    "WAR_DEAD_CATACOMBS",
    "GIANT_CONQUERING_HEROS_GRAVE",
    "GIANTS_MOUNTAINTOP_CATACOMBS",
    "CONSECRATED_SNOWFIELD_CATACOMBS",
    "HIDDEN_PATH_TO_THE_HALIGTREE",
    "MURKWATER_CAVE",
    "EARTHBORE_CAVE",
    "TOMBSWARD_CAVE",
    "GROVESIDE_CAVE",
    "STILLWATER_CAVE",
    "LAKESIDE_CRYSTAL_CAVE",
    "ACADEMY_CRYSTAL_CAVE",
    "SEETHEWATER_CAVE",
    "VOLCANO_CAVE",
    "DRAGONBARROW_CAVE",
    "SELLIA_HIDEAWAY",
    "CAVE_OF_THE_FORLORN",
    "COASTAL_CAVE",
    "HIGHROAD_CAVE",
    "PERFUMERS_GROTTO",
    "SAGES_CAVE",
    "ABANDONED_CAVE",
    "GAOL_CAVE",
    "SPIRITCALLER_CAVE",
    "MORNE_TUNNEL",
    "LIMGRAVE_TUNNELS",
    "RAYA_LUCARIA_CRYSTAL_TUNNEL",
    "OLD_ALTUS_TUNNEL",
    "ALTUS_TUNNEL",
    "GAEL_TUNNEL",
    "SELLIA_CRYSTAL_TUNNEL",
    "YELOUGH_ANIX_TUNNEL",
    "DIVINE_TOWER_OF_LIMGRAVE",
    "DIVINE_TOWER_OF_LIURNIA",
    "DIVINE_TOWER_OF_WEST_ALTUS",
    "DIVINE_TOWER_OF_CAELID",
    "DIVINE_TOWER_OF_EAST_ALTUS",
    "ISOLATED_DIVINE_TOWER",

    # Overworld
    "SOUTHWEST_LIURNIA",
    "SOUTHWEST_LIURNIA_SW",
    "SOUTHWEST_LIURNIA_SW_SE",
    "SOUTHWEST_LIURNIA_SW_NE",
    "SOUTHWEST_LIURNIA_NW",
    "SOUTHWEST_LIURNIA_NW_SE",
    "SOUTHWEST_LIURNIA_NW_NE",
    "SOUTHWEST_LIURNIA_SE",
    "SOUTHWEST_LIURNIA_SE_NW",
    "SOUTHWEST_LIURNIA_SE_NE",
    "SOUTHWEST_LIURNIA_NE",
    "SOUTHWEST_LIURNIA_NE_SW",
    "SOUTHWEST_LIURNIA_NE_NW",
    "SOUTHWEST_LIURNIA_NE_SE",
    "SOUTHWEST_LIURNIA_NE_NE",
    "WEST_LIURNIA",
    "WEST_LIURNIA_SW",
    "WEST_LIURNIA_SW_SE",
    "WEST_LIURNIA_SW_NE",
    "WEST_LIURNIA_NW",
    "WEST_LIURNIA_NW_SE",
    "WEST_LIURNIA_NW_NE",
    "WEST_LIURNIA_SE",
    "WEST_LIURNIA_SE_SW",
    "WEST_LIURNIA_SE_NW",
    "WEST_LIURNIA_SE_SE",
    "WEST_LIURNIA_SE_NE",
    "WEST_LIURNIA_NE",
    "WEST_LIURNIA_NE_SW",
    "WEST_LIURNIA_NE_NW",
    "WEST_LIURNIA_NE_SE",
    "WEST_LIURNIA_NE_NE",
    "NORTHWEST_LIURNIA",
    "NORTHWEST_LIURNIA_SE",
    "NORTHWEST_LIURNIA_SE_SW",
    "NORTHWEST_LIURNIA_SE_NW",
    "NORTHWEST_LIURNIA_SE_SE",
    "NORTHWEST_LIURNIA_SE_NE",
    "NORTHWEST_LIURNIA_NE",
    "NORTHWEST_LIURNIA_NE_SW",
    "NORTHWEST_LIURNIA_NE_NW",
    "NORTHWEST_LIURNIA_NE_SE",
    "NORTHWEST_LIURNIA_NE_NE",
    "FAR_WEST_ALTUS_PLATEAU",
    "FAR_WEST_ALTUS_PLATEAU_SE",
    "FAR_WEST_ALTUS_PLATEAU_SE_SE",
    "FAR_WEST_ALTUS_PLATEAU_SE_NE",
    "FAR_WEST_ALTUS_PLATEAU_NE",
    "FAR_WEST_ALTUS_PLATEAU_NE_SE",
    "FAR_WEST_LIMGRAVE",
    "FAR_WEST_LIMGRAVE_NE",
    "FAR_WEST_LIMGRAVE_NE_NW",
    "FAR_WEST_LIMGRAVE_NE_NE",
    "SOUTHEAST_LIURNIA",
    "SOUTHEAST_LIURNIA_SW",
    "SOUTHEAST_LIURNIA_SW_NW",
    "SOUTHEAST_LIURNIA_SW_NE",
    "SOUTHEAST_LIURNIA_NW",
    "SOUTHEAST_LIURNIA_NW_SW",
    "SOUTHEAST_LIURNIA_NW_NW",
    "SOUTHEAST_LIURNIA_NW_SE",
    "SOUTHEAST_LIURNIA_NW_NE",
    "SOUTHEAST_LIURNIA_SE",
    "SOUTHEAST_LIURNIA_SE_SW",
    "SOUTHEAST_LIURNIA_SE_NW",
    "SOUTHEAST_LIURNIA_SE_SE",
    "SOUTHEAST_LIURNIA_SE_NE",
    "SOUTHEAST_LIURNIA_NE",
    "SOUTHEAST_LIURNIA_NE_SW",
    "SOUTHEAST_LIURNIA_NE_NW",
    "SOUTHEAST_LIURNIA_NE_SE",
    "SOUTHEAST_LIURNIA_NE_NE",
    "EAST_LIURNIA",
    "EAST_LIURNIA_SW",
    "EAST_LIURNIA_SW_SW",
    "EAST_LIURNIA_SW_NW",
    "EAST_LIURNIA_SW_SE",
    "EAST_LIURNIA_SW_NE",
    "EAST_LIURNIA_NW",
    "EAST_LIURNIA_NW_SW",
    "EAST_LIURNIA_NW_NW",
    "EAST_LIURNIA_NW_SE",
    "EAST_LIURNIA_NW_NE",
    "EAST_LIURNIA_SE",
    "EAST_LIURNIA_SE_SW",
    "EAST_LIURNIA_SE_NW",
    "EAST_LIURNIA_SE_SE",
    "EAST_LIURNIA_SE_NE",
    "EAST_LIURNIA_NE",
    "EAST_LIURNIA_NE_SW",
    "EAST_LIURNIA_NE_NW",
    "EAST_LIURNIA_NE_SE",
    "LIURNIA_TO_ALTUS_PLATEAU",
    "LIURNIA_TO_ALTUS_PLATEAU_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_SW_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_NW_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_SE_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_NE",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_SW",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_NW",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_SE",
    "LIURNIA_TO_ALTUS_PLATEAU_NE_NE",
    "WEST_ALTUS_PLATEAU",
    "WEST_ALTUS_PLATEAU_SW",
    "WEST_ALTUS_PLATEAU_SW_SW",
    "WEST_ALTUS_PLATEAU_SW_NW",
    "WEST_ALTUS_PLATEAU_SW_SE",
    "WEST_ALTUS_PLATEAU_SW_NE",
    "WEST_ALTUS_PLATEAU_NW",
    "WEST_ALTUS_PLATEAU_NW_SW",
    "WEST_ALTUS_PLATEAU_NW_SE",
    "WEST_ALTUS_PLATEAU_NW_NE",
    "WEST_ALTUS_PLATEAU_SE",
    "WEST_ALTUS_PLATEAU_SE_SW",
    "WEST_ALTUS_PLATEAU_SE_NW",
    "WEST_ALTUS_PLATEAU_SE_SE",
    "WEST_ALTUS_PLATEAU_SE_NE",
    "WEST_ALTUS_PLATEAU_NE",
    "WEST_ALTUS_PLATEAU_NE_SW",
    "WEST_ALTUS_PLATEAU_NE_SE",
    "SOUTH_WEEPING_PENINSULA",
    "SOUTH_WEEPING_PENINSULA_NE",
    "SOUTH_WEEPING_PENINSULA_NE_SE",
    "SOUTH_WEEPING_PENINSULA_NE_NE",
    "WEST_WEEPING_PENINSULA",
    "WEST_WEEPING_PENINSULA_SW",
    "WEST_WEEPING_PENINSULA_SW_NW",
    "WEST_WEEPING_PENINSULA_SW_SE",
    "WEST_WEEPING_PENINSULA_SW_NE",
    "WEST_WEEPING_PENINSULA_NW",
    "WEST_WEEPING_PENINSULA_NW_SE",
    "WEST_WEEPING_PENINSULA_NW_NE",
    "WEST_WEEPING_PENINSULA_SE",
    "WEST_WEEPING_PENINSULA_SE_SW",
    "WEST_WEEPING_PENINSULA_SE_NW",
    "WEST_WEEPING_PENINSULA_SE_SE",
    "WEST_WEEPING_PENINSULA_SE_NE",
    "WEST_WEEPING_PENINSULA_NE",
    "WEST_WEEPING_PENINSULA_NE_SW",
    "WEST_WEEPING_PENINSULA_NE_NW",
    "WEST_WEEPING_PENINSULA_NE_SE",
    "WEST_WEEPING_PENINSULA_NE_NE",
    "WEST_LIMGRAVE",
    "WEST_LIMGRAVE_SW",
    "WEST_LIMGRAVE_SW_SE",
    "WEST_LIMGRAVE_SW_NE",
    "WEST_LIMGRAVE_NW",
    "WEST_LIMGRAVE_NW_SW",
    "WEST_LIMGRAVE_NW_NW",
    "WEST_LIMGRAVE_NW_SE",
    "WEST_LIMGRAVE_NW_NE",
    "WEST_LIMGRAVE_SE",
    "WEST_LIMGRAVE_SE_SW",
    "WEST_LIMGRAVE_SE_NW",
    "WEST_LIMGRAVE_SE_SE",
    "WEST_LIMGRAVE_SE_NE",
    "WEST_LIMGRAVE_NE",
    "WEST_LIMGRAVE_NE_SW",
    "WEST_LIMGRAVE_NE_NW",
    "WEST_LIMGRAVE_NE_SE",
    "WEST_LIMGRAVE_NE_NE",
    "NORTHWEST_LIMGRAVE_COAST",
    "NORTHWEST_LIMGRAVE_COAST_SW",
    "NORTHWEST_LIMGRAVE_COAST_SW_SW",
    "NORTHWEST_LIMGRAVE_COAST_SE",
    "NORTHWEST_LIMGRAVE_COAST_SE_SW",
    "NORTHWEST_LIMGRAVE_COAST_SE_SE",
    "SOUTH_ALTUS_PLATEAU",
    "SOUTH_ALTUS_PLATEAU_NW",
    "SOUTH_ALTUS_PLATEAU_NW_SW",
    "SOUTH_ALTUS_PLATEAU_NW_NW",
    "SOUTH_ALTUS_PLATEAU_NW_SE",
    "SOUTH_ALTUS_PLATEAU_NW_NE",
    "SOUTH_ALTUS_PLATEAU_NE",
    "SOUTH_ALTUS_PLATEAU_NE_SW",
    "SOUTH_ALTUS_PLATEAU_NE_NW",
    "SOUTH_ALTUS_PLATEAU_NE_SE",
    "SOUTH_ALTUS_PLATEAU_NE_NE",
    "NORTH_ALTUS_PLATEAU",
    "NORTH_ALTUS_PLATEAU_SW",
    "NORTH_ALTUS_PLATEAU_SW_SW",
    "NORTH_ALTUS_PLATEAU_SW_NW",
    "NORTH_ALTUS_PLATEAU_SW_SE",
    "NORTH_ALTUS_PLATEAU_SW_NE",
    "NORTH_ALTUS_PLATEAU_NW",
    "NORTH_ALTUS_PLATEAU_NW_SW",
    "NORTH_ALTUS_PLATEAU_NW_NW",
    "NORTH_ALTUS_PLATEAU_NW_SE",
    "NORTH_ALTUS_PLATEAU_NW_NE",
    "NORTH_ALTUS_PLATEAU_SE",
    "NORTH_ALTUS_PLATEAU_SE_SW",
    "NORTH_ALTUS_PLATEAU_SE_NW",
    "NORTH_ALTUS_PLATEAU_SE_SE",
    "NORTH_ALTUS_PLATEAU_SE_NE",
    "NORTH_ALTUS_PLATEAU_NE",
    "NORTH_ALTUS_PLATEAU_NE_SW",
    "NORTH_ALTUS_PLATEAU_NE_NW",
    "NORTH_ALTUS_PLATEAU_NE_SE",
    "SOUTHEAST_WEEPING_PENINSULA_COAST",
    "SOUTHEAST_WEEPING_PENINSULA_COAST_NW",
    "SOUTHEAST_WEEPING_PENINSULA_COAST_NW_NW",
    "EAST_WEEPING_PENINSULA",
    "EAST_WEEPING_PENINSULA_SW",
    "EAST_WEEPING_PENINSULA_SW_SW",
    "EAST_WEEPING_PENINSULA_SW_NW",
    "EAST_WEEPING_PENINSULA_SW_SE",
    "EAST_WEEPING_PENINSULA_SW_NE",
    "EAST_WEEPING_PENINSULA_NW",
    "EAST_WEEPING_PENINSULA_NW_SW",
    "EAST_WEEPING_PENINSULA_NW_NW",
    "EAST_WEEPING_PENINSULA_NW_SE",
    "EAST_WEEPING_PENINSULA_NW_NE",
    "EAST_LIMGRAVE",
    "EAST_LIMGRAVE_SW",
    "EAST_LIMGRAVE_SW_SW",
    "EAST_LIMGRAVE_SW_NW",
    "EAST_LIMGRAVE_SW_SE",
    "EAST_LIMGRAVE_SW_NE",
    "EAST_LIMGRAVE_NW",
    "EAST_LIMGRAVE_NW_SW",
    "EAST_LIMGRAVE_NW_NW",
    "EAST_LIMGRAVE_NW_SE",
    "EAST_LIMGRAVE_NW_NE",
    "EAST_LIMGRAVE_SE",
    "EAST_LIMGRAVE_SE_SW",
    "EAST_LIMGRAVE_SE_NW",
    "EAST_LIMGRAVE_SE_NE",
    "EAST_LIMGRAVE_NE",
    "EAST_LIMGRAVE_NE_SW",
    "EAST_LIMGRAVE_NE_NW",
    "EAST_LIMGRAVE_NE_SE",
    "EAST_LIMGRAVE_NE_NE",
    "NORTHWEST_CAELID",
    "NORTHWEST_CAELID_SW",
    "NORTHWEST_CAELID_SW_SE",
    "NORTHWEST_CAELID_SE",
    "NORTHWEST_CAELID_SE_SW",
    "NORTHWEST_CAELID_SE_SE",
    "NORTHWEST_CAELID_SE_NE",
    "NORTHWEST_CAELID_NE",
    "NORTHWEST_CAELID_NE_SE",
    "SOUTHEAST_ALTUS_PLATEAU",
    "SOUTHEAST_ALTUS_PLATEAU_NW",
    "SOUTHEAST_ALTUS_PLATEAU_NW_NE",
    "SOUTHEAST_ALTUS_PLATEAU_NE",
    "SOUTHEAST_ALTUS_PLATEAU_NE_NE",
    "NORTHEAST_ALTUS_PLATEAU",
    "NORTHEAST_ALTUS_PLATEAU_SW",
    "NORTHEAST_ALTUS_PLATEAU_SW_SW",
    "NORTHEAST_ALTUS_PLATEAU_SW_NW",
    "NORTHEAST_ALTUS_PLATEAU_SW_SE",
    "NORTHEAST_ALTUS_PLATEAU_SW_NE",
    "NORTHEAST_ALTUS_PLATEAU_NE",
    "NORTHEAST_ALTUS_PLATEAU_NE_NW",
    "NORTHEAST_ALTUS_PLATEAU_NE_NE",
    "WEST_CONSECRATED_SNOWFIELD",
    "WEST_CONSECRATED_SNOWFIELD_SE",
    "WEST_CONSECRATED_SNOWFIELD_SE_NW",
    "WEST_CONSECRATED_SNOWFIELD_SE_SE",
    "WEST_CONSECRATED_SNOWFIELD_SE_NE",
    "WEST_CONSECRATED_SNOWFIELD_NE",
    "WEST_CONSECRATED_SNOWFIELD_NE_SE",
    "FAR_SOUTH_CAELID",
    "FAR_SOUTH_CAELID_NE",
    "FAR_SOUTH_CAELID_NE_NE",
    "SOUTH_CAELID",
    "SOUTH_CAELID_SW",
    "SOUTH_CAELID_SW_SW",
    "SOUTH_CAELID_SW_NW",
    "SOUTH_CAELID_SW_SE",
    "SOUTH_CAELID_SW_NE",
    "SOUTH_CAELID_NW",
    "SOUTH_CAELID_NW_SW",
    "SOUTH_CAELID_NW_NW",
    "SOUTH_CAELID_NW_SE",
    "SOUTH_CAELID_NW_NE",
    "SOUTH_CAELID_SE",
    "SOUTH_CAELID_SE_SW",
    "SOUTH_CAELID_SE_NW",
    "SOUTH_CAELID_SE_SE",
    "SOUTH_CAELID_SE_NE",
    "SOUTH_CAELID_NE",
    "SOUTH_CAELID_NE_SW",
    "SOUTH_CAELID_NE_NW",
    "SOUTH_CAELID_NE_SE",
    "SOUTH_CAELID_NE_NE",
    "NORTH_CAELID",
    "NORTH_CAELID_SW",
    "NORTH_CAELID_SW_SW",
    "NORTH_CAELID_SW_NW",
    "NORTH_CAELID_SW_SE",
    "NORTH_CAELID_SW_NE",
    "NORTH_CAELID_SE",
    "NORTH_CAELID_SE_SW",
    "NORTH_CAELID_SE_NW",
    "NORTH_CAELID_SE_SE",
    "NORTH_CAELID_SE_NE",
    "NORTH_CAELID_NE",
    "NORTH_CAELID_NE_SE",
    "NORTH_CAELID_NE_NE",
    "FORBIDDEN_LANDS",
    "FORBIDDEN_LANDS_NW",
    "FORBIDDEN_LANDS_NW_NW",
    "SOUTHWEST_MOUNTAINTOPS",
    "SOUTHWEST_MOUNTAINTOPS_SW",
    "SOUTHWEST_MOUNTAINTOPS_SW_SE",
    "SOUTHWEST_MOUNTAINTOPS_SW_NE",
    "SOUTHWEST_MOUNTAINTOPS_NW",
    "SOUTHWEST_MOUNTAINTOPS_NW_SW",
    "SOUTHWEST_MOUNTAINTOPS_NW_NW",
    "SOUTHWEST_MOUNTAINTOPS_NW_SE",
    "SOUTHWEST_MOUNTAINTOPS_NW_NE",
    "SOUTHWEST_MOUNTAINTOPS_SE",
    "SOUTHWEST_MOUNTAINTOPS_SE_NW",
    "SOUTHWEST_MOUNTAINTOPS_SE_SE",
    "SOUTHWEST_MOUNTAINTOPS_SE_NE",
    "SOUTHWEST_MOUNTAINTOPS_NE",
    "SOUTHWEST_MOUNTAINTOPS_NE_SW",
    "SOUTHWEST_MOUNTAINTOPS_NE_NW",
    "SOUTHWEST_MOUNTAINTOPS_NE_SE",
    "SOUTHWEST_MOUNTAINTOPS_NE_NE",
    "NORTHWEST_MOUNTAINTOPS",
    "NORTHWEST_MOUNTAINTOPS_SW",
    "NORTHWEST_MOUNTAINTOPS_SW_SW",
    "NORTHWEST_MOUNTAINTOPS_SW_NW",
    "NORTHWEST_MOUNTAINTOPS_SW_SE",
    "NORTHWEST_MOUNTAINTOPS_SW_NE",
    "NORTHWEST_MOUNTAINTOPS_NW",
    "NORTHWEST_MOUNTAINTOPS_NW_SW",
    "NORTHWEST_MOUNTAINTOPS_SE",
    "NORTHWEST_MOUNTAINTOPS_SE_SW",
    "NORTHWEST_MOUNTAINTOPS_SE_NW",
    "NORTHWEST_MOUNTAINTOPS_SE_SE",
    "NORTHWEST_MOUNTAINTOPS_SE_NE",
    "NORTHWEST_MOUNTAINTOPS_NE",
    "NORTHWEST_MOUNTAINTOPS_NE_SE",
    "SOUTHEAST_CAELID",
    "SOUTHEAST_CAELID_SW",
    "SOUTHEAST_CAELID_SW_NW",
    "SOUTHEAST_CAELID_NW",
    "SOUTHEAST_CAELID_NW_SW",
    "SOUTHEAST_CAELID_NW_NW",
    "SOUTHEAST_CAELID_NW_SE",
    "SOUTHEAST_CAELID_NW_NE",
    "NORTHEAST_CAELID",
    "NORTHEAST_CAELID_SW",
    "NORTHEAST_CAELID_SW_SW",
    "NORTHEAST_CAELID_SW_NW",
    "NORTHEAST_CAELID_NW",
    "NORTHEAST_CAELID_NW_SW",
    "NORTHEAST_CAELID_NW_NW",
    "SOUTHEAST_MOUNTAINTOPS",
    "SOUTHEAST_MOUNTAINTOPS_SW",
    "SOUTHEAST_MOUNTAINTOPS_SW_SW",
    "SOUTHEAST_MOUNTAINTOPS_SW_NW",
    "SOUTHEAST_MOUNTAINTOPS_SW_SE",
    "SOUTHEAST_MOUNTAINTOPS_SW_NE",
    "SOUTHEAST_MOUNTAINTOPS_NW",
    "SOUTHEAST_MOUNTAINTOPS_NW_SW",
    "SOUTHEAST_MOUNTAINTOPS_NW_NW",
    "SOUTHEAST_MOUNTAINTOPS_NW_SE",
    "SOUTHEAST_MOUNTAINTOPS_NW_NE",
    "SOUTHEAST_MOUNTAINTOPS_SE",
    "SOUTHEAST_MOUNTAINTOPS_SE_NW",
    "SOUTHEAST_MOUNTAINTOPS_NE",
    "SOUTHEAST_MOUNTAINTOPS_NE_NW",
    "NORTHEAST_MOUNTAINTOPS",
    "NORTHEAST_MOUNTAINTOPS_SW",
    "NORTHEAST_MOUNTAINTOPS_SW_SW",
    "NORTHEAST_MOUNTAINTOPS_SW_NW",
    "NORTHEAST_MOUNTAINTOPS_SW_SE",
    "NORTHEAST_MOUNTAINTOPS_SW_NE",
    "NORTHEAST_MOUNTAINTOPS_NW",
    "NORTHEAST_MOUNTAINTOPS_NW_SW",
    "NORTHEAST_MOUNTAINTOPS_NW_SE",
    "NORTHEAST_MOUNTAINTOPS_SE",
    "NORTHEAST_MOUNTAINTOPS_SE_SW",
    "NORTHEAST_MOUNTAINTOPS_SE_NW",
    "EAST_LIMGRAVE_METEOR",
    "EAST_LIMGRAVE_METEOR_SW",
    "EAST_LIMGRAVE_METEOR_SW_SE",
    "NORTHEAST_ALTUS_PLATEAU_ASHEN",
    "NORTHEAST_ALTUS_PLATEAU_ASHEN_SW",
    "NORTHEAST_ALTUS_PLATEAU_ASHEN_SW_SE",
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
    "AIStatusType",
    "ArenaMatchType",
    "ArenaResult",
    "BitOperation",
    "BossMusicState",
    "ButtonType",
    "CharacterType",
    "CharacterUpdateRate",
    "ClassType",
    "ComparisonType",
    "CutsceneFlags",
    "DamageTargetType",
    "EventReturnType",
    "FlagSetting",
    "FlagType",
    "InterpolationState",
    "ItemType",
    "RangeState",
    "CoordEntityType",
    "NavmeshType",
    "NumberButtons",
    "OnOffChange",
    "OnRestBehavior",
    "SoundType",
    "StatueType",
    "SummonSignType",
    "TriggerAttribute",
    "UpdateAuthority",
    "Weather",
    "ArmorType",
    "BannerType",
    "CalculationType",
    "ClientType",
    "ConditionGroup",
    "DamageType",
    "DeleteOrAdd",
    "DialogResult",
    "DisplayState",
    "DoorState",
    "Gender",
    "Label",
    "MultiplayerState",
    "NPCPartType",
    "SingleplayerSummonSignType",
    "TeamType",
]

from ..maps import constants
from ..maps.constants import *
from .emevd import EMEVD, decompiler, enums
from .emevd.enums import *
from .event_directory import EventDirectory
from .utilities import convert_events, compare_events
