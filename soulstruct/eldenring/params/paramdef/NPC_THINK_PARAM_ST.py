from __future__ import annotations

__all__ = ["NPC_THINK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NPC_THINK_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    LogicID: int = ParamField(
        int, "logicId", game_type=LogicAIScript, default=-1,
        tooltip="ID of logic (non-battle) Lua script.",
    )
    BattleID: int = ParamField(
        int, "battleGoalID", game_type=BattleAIScript, default=-1,
        tooltip="Battle goal ID used to look up battle Lua script.",
    )
    SearchEyedist: int = ParamField(
        ushort, "searchEye_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SearchEyeangY: int = ParamField(
        byte, "searchEye_angY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNoAvoidHugeEnemy: bool = ParamField(
        byte, "isNoAvoidHugeEnemy:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWeaponOnOff: bool = ParamField(
        byte, "enableWeaponOnOff:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    TargetAILockDmyPoly: bool = ParamField(
        byte, "targetAILockDmyPoly:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad8:5", bit_count=5)
    SpEffectIdRangedAttack: int = ParamField(
        int, "spEffectId_RangedAttack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetLv1ForgetTime: float = ParamField(
        float, "searchTargetLv1ForgetTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetLv2ForgetTime: float = ParamField(
        float, "searchTargetLv2ForgetTime", default=8.0,
        tooltip="TOOLTIP-TODO",
    )
    RetreatTimeAfterHittingEnemyWall: float = ParamField(
        float, "BackHomeLife_OnHitEneWal", default=5.0,
        tooltip="Retreat goal time when touching an 'enemy wall' that blocks the NPC's path. (Not clear what an "
                "'enemy wall' means. Almost always set to 5 (rarely 6).",
    )
    SightForgetTime: float = ParamField(
        float, "SightTargetForgetTime", default=600.0,
        tooltip="Time to forget about sighted targets. Usually set to 600.",
    )
    StuckAnimationID: int = ParamField(
        int, "idAttackCannotMove", default=0,
        tooltip="Animation to use if the NPC gets stuck on a destructible object. Usually 3000 (basic attack).",
    )
    HearingDistance: float = ParamField(
        float, "ear_dist", default=0.0,
        tooltip="Distance of NPC hearing (in meters).",
    )
    HelpCallResponseAnimation: int = ParamField(
        int, "callHelp_ActionAnimId", game_type=Animation, default=-1,
        tooltip="Animation to play when responding to a call for help. Usually set to -1 for NPCs who can reply to "
                "calls for help, which I assume means no animation is played. Set to 0 for NPCs who ignore calls for "
                "help.",
    )
    HelpCallSendAnimation: int = ParamField(
        int, "callHelp_CallActionId", default=-1,
        tooltip="Animation to play when calling for help. Only used by Female Ghost (7300) and Male Ghost and summons "
                "(-1). I assume -1 means no animation is played. Set to 0 for all other NPCs.",
    )
    SightDistance: int = ParamField(
        ushort, "eye_dist", default=0,
        tooltip="Distance of NPC eyesight (in meters).",
    )
    IsGuardAct: int = ParamField(
        byte, "isGuard_Act", BOOL_DODONT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad6[1]")
    HearingCutDistance: int = ParamField(
        ushort, "ear_soundcut_dist", default=0,
        tooltip="Internal description: 'Distance to reduce the size of the sound source. Sounds less than this "
                "distance will not be heard.' Set to 1 for Bloatheads and Bloathead Sorcerers and 0 for everyone "
                "else.",
    )
    SmellDistance: int = ParamField(
        ushort, "nose_dist", default=0,
        tooltip="Distance of NPC smell (auto-detect).",
    )
    MaxRetreatDistance: int = ParamField(
        ushort, "maxBackhomeDist", default=0,
        tooltip="Absolute furthest the NPC can travel from their nest before retreating, in or out of battle. "
                "(Argument of internal GOAL function 'COMMON_SetBattleActLogic()'.) Usually set to about 50% more "
                "than BattleRetreatDistance.",
    )
    BattleRetreatDistance: int = ParamField(
        ushort, "backhomeDist", default=0,
        tooltip="Furthest distance the NPC can travel from their nest before retreating in battle. (Argument of "
                "internal GOAL function 'COMMON_SetBattleActLogic()'.)",
    )
    RetreatBattleStartDistance: int = ParamField(
        ushort, "backhomeBattleDist", default=0,
        tooltip="Target distance at which battle mode is triggered while the enemy is retreating. (Argument of "
                "internal GOAL function 'COMMON_SetBattleActLogic()'.)",
    )
    NonBattleActLife: int = ParamField(
        ushort, "nonBattleActLife", default=0,
        tooltip="Lifespan of Acts outside of battle. Set to 10 for Bloatheads and Bloathead Sorcerers, 0 for "
                "Priscilla's Tail and the Bed of Chaos bug, and 5 for everyone else. (Argument of internal GOAL "
                "function 'COMMON_SetBattleActLogic()'.)",
    )
    SearchTimeBeforeRetreat: int = ParamField(
        ushort, "BackHome_LookTargetTime", default=3,
        tooltip="Time that NPC will search for a lost target before retreating (I think). Set to 20 for everyone "
                "except the Bounding Demons of Izalith, who have a value of 0.",
    )
    SearchDistanceBeforeRetreat: int = ParamField(
        ushort, "BackHome_LookTargetDist", default=10,
        tooltip="Distance that NPC will search for a lost target before retreating (I think). Set to 20 for everyone "
                "except the Bounding Demons of Izalith, who have a value of 0.",
    )
    HearingForgetTime: float = ParamField(
        float, "SoundTargetForgetTime", default=3.0,
        tooltip="Time to forget about heard targets. Usually set to 300.",
    )
    BattleStartDistance: int = ParamField(
        ushort, "BattleStartDist", default=0,
        tooltip="Target distance at which battle mode is triggered.",
    )
    HelpGroupID: int = ParamField(
        ushort, "callHelp_MyPeerId", default=0,
        tooltip="Determines which calls for help this NPC will respond to (must match caller's HelpCallGroupID). Only "
                "0 (no ID) and 1 are used.",
    )
    HelpCallGroupID: int = ParamField(
        ushort, "callHelp_CallPeerId", default=0,
        tooltip="HelpGroupID value of NPCs who should respond to calls for help by this NPC. Only 0 (no ID) and 1 are "
                "used.",
    )
    TargetSysDamageRate: int = ParamField(
        ushort, "targetSys_DmgEffectRate", default=100,
        tooltip="Internal description: 'Get damage rate (%) for target system evaluation information.' Set to 0 for "
                "summons, phantoms, and the Parasitic Wall Hugger, and 100 for everyone else.",
    )
    TeamAttackEffectivity: int = ParamField(
        byte, "TeamAttackEffectivity", default=25,
        tooltip="Value from 0 to 100 that determines the number of simultaneous attacks made by this NPC's team. "
                "Higher values mean that less members of this team can participate in attacks at the same time. (I "
                "presume that the total score of attacking team members cannot exceed 100.) Usually set to 25 or 100.",
    )
    SightRangeHeight: int = ParamField(
        byte, "eye_angX", default=0,
        tooltip="Angular width of sight field in degrees.",
    )
    SightRangeWidth: int = ParamField(
        byte, "eye_angY", default=0,
        tooltip="Angular height of sight field in degrees.",
    )
    DisableDark: int = ParamField(
        byte, "disableDark", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaravanRole: int = ParamField(
        byte, "caravanRole", NPC_THINK_CARAVAN_ROLE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallTargetMinDistance: int = ParamField(
        byte, "callHelp_CallValidMinDistTarget", default=5,
        tooltip="Minimum distance from AI target for help call to be made. Always zero.",
    )
    HelpCallFriendMaxDistance: int = ParamField(
        byte, "callHelp_CallValidRange", default=15,
        tooltip="Maximum distance of friend to receive help call from this NPC. Set to 50 for both Male and Female "
                "Ghosts, and 0 for everyone else.",
    )
    HelpCallForgetTime: int = ParamField(
        byte, "callHelp_ForgetTimeByArrival", default=0,
        tooltip="Time until call for help is forgotten by responder.",
    )
    HelpCallMinWaitTime: int = ParamField(
        byte, "callHelp_MinWaitTime", default=0,
        tooltip="Internal description: 'Minimum time for response goal at first waiting goal'. Units are in tenths of "
                "a second. Only used for Male Ghosts (20).",
    )
    HelpCallMaxWaitTime: int = ParamField(
        byte, "callHelp_MaxWaitTime", default=0,
        tooltip="Internal description: 'Maximum time for response goal at first waiting goal'. Units are in tenths of "
                "a second. Only used for Female Ghosts (40).",
    )
    CautionGoalAction: int = ParamField(
        byte, "goalAction_ToCaution", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="Type of action taken when AI enters the 'Caution' state.",
    )
    EarlistenLevel: int = ParamField(
        byte, "ear_listenLevel", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallReplyType: int = ParamField(
        byte, "callHelp_ReplyBehaviorType", NPC_THINK_REPLY_BEHAVIOR_TYPE, default=0,
        tooltip="Set to 0 for NPCs who do not reply to calls for help and 1 for NPCs who do.",
    )
    IgnoreNavmesh: int = ParamField(
        byte, "disablePathMove", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="If 1, this NPC will ignore navmesh when moving. True for Ghosts and enemies that don't move at all.",
    )
    SkipArrivalVisibleCheck: int = ParamField(
        byte, "skipArrivalVisibleCheck", ON_OFF, default=0,
        tooltip="Internal description: 'If enabled, arrival determination is performed even if the line of sightis "
                "not passed.' True only for Hawkeye Gough.",
    )
    AdmirerAttribute: int = ParamField(
        byte, "thinkAttr_doAdmirer", ON_OFF, default=0,
        tooltip="Internal description: 'Thought attribute: when enabled, it plays the role of a wrap.' I don'tknow "
                "exactly what that means, but this is likely important for something. Enabled for Soulmassand "
                "Pursuers, non-giant Rats, Infested Ghouls, Mushrooms, most Hollows (not archers), MaleGhosts, normal "
                "Skeletons and Skeleton Beasts, and Pisaca.",
    )
    CanFallOffEdges: bool = ParamField(
        byte, "enableNaviFlg_Edge:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="If True, this NPC will pursue targets off navmesh edges (survivable falls).",
    )
    CanNavigateWideSpaces: bool = ParamField(
        byte, "enableNaviFlg_LargeSpace:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="If True, this NPC can enter navmesh regions flagged as 'large spaces'.",
    )
    CanNavigateLadders: bool = ParamField(
        byte, "enableNaviFlg_Ladder:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="If True, this NPC will use ladders.",
    )
    CanNavigateHoles: bool = ParamField(
        byte, "enableNaviFlg_Hole:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="If True, this NPC can fall into navmesh holes.",
    )
    CanNavigateDoors: bool = ParamField(
        byte, "enableNaviFlg_Door:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="If True, this NPC can go through doors (but not necessarily open closed doors).",
    )
    CanNavigateInsideWalls: bool = ParamField(
        byte, "enableNaviFlg_InSideWall:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="If True, this NPC can go through walls (i.e. ignores navmesh walls).",
    )
    EnableNaviFlgLava: bool = ParamField(
        byte, "enableNaviFlg_Lava:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanNavigateOrdinaryEdges: bool = ParamField(
        byte, "enableNaviFlg_Edge_Ordinary:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TODO",
    )
    _Pad2: bytes = ParamPad(3, "enableNaviFlg_reserve1[3]")
    SearchThresholdLv0toLv1: int = ParamField(
        int, "searchThreshold_Lv0toLv1", default=10,
        tooltip="TOOLTIP-TODO",
    )
    SearchThresholdLv1toLv2: int = ParamField(
        int, "searchThreshold_Lv1toLv2", default=70,
        tooltip="TOOLTIP-TODO",
    )
    PlatoonReplyTime: float = ParamField(
        float, "platoonReplyTime", default=0.0,
        tooltip="TODO",
    )
    PlatoonReplyRandomExtraTime: float = ParamField(
        float, "platoonReplyAddRandomTime", default=0.0,
        tooltip="TODO",
    )
    SearchEyeangX: int = ParamField(
        byte, "searchEye_angX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUpdateBattleSight: int = ParamField(
        byte, "isUpdateBattleSight", BOOL_DODONT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleEyeupdateDist: int = ParamField(
        ushort, "battleEye_updateDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleEyeupdateAngX: int = ParamField(
        byte, "battleEye_updateAngX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleEyeupdateAngY: int = ParamField(
        byte, "battleEye_updateAngY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(16, "pad4[16]")
    SightBackOffsetDistance: int = ParamField(
        ushort, "eye_BackOffsetDist", default=0,
        tooltip="TODO",
    )
    SightBeginDistance: int = ParamField(
        ushort, "eye_BeginDist", default=0,
        tooltip="TODO",
    )
    ActTypeOnFailedPath: int = ParamField(
        byte, "actTypeOnFailedPath", NPC_THINK_ACTTYPE_ON_FAILEDPATH, default=0,
        tooltip="TODO",
    )
    GoalActionToCautionImportant: int = ParamField(
        byte, "goalAction_ToCautionImportant", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShiftAnimeIdRangedAttack: int = ParamField(
        int, "shiftAnimeId_RangedAttack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActTypeOnNonBtlFailedPath: int = ParamField(
        byte, "actTypeOnNonBtlFailedPath", NPC_THINK_ACTTYPE_ON_NONBTL_FAILEDPATH, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBuddyAI: int = ParamField(
        byte, "isBuddyAI", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToSearchLv1: int = ParamField(
        byte, "goalAction_ToSearchLv1", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToSearchLv2: int = ParamField(
        byte, "goalAction_ToSearchLv2", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableJumpMove: int = ParamField(
        byte, "enableJumpMove", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableLocalSteering: int = ParamField(
        byte, "disableLocalSteering", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TODO",
    )
    DisappearGoalAction: int = ParamField(
        byte, "goalAction_ToDisappear", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TODO",
    )
    ChangeStateActionToNormal: int = ParamField(
        byte, "changeStateAction_ToNormal", NPC_THINK_CHANGE_STATE_ACTION, default=0,
        tooltip="TODO",
    )
    MemoryTargetForgetTime: float = ParamField(
        float, "MemoryTargetForgetTime", default=150.0,
        tooltip="TOOLTIP-TODO",
    )
    RangedAttackId: int = ParamField(
        int, "rangedAttackId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseFallonNormalCaution: int = ParamField(
        byte, "useFall_onNormalCaution", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=2,
        tooltip="TOOLTIP-TODO",
    )
    UseFallonSearchBattle: int = ParamField(
        byte, "useFall_onSearchBattle", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=2,
        tooltip="TOOLTIP-TODO",
    )
    EnableJumpMoveonBattle: int = ParamField(
        byte, "enableJumpMove_onBattle", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BackToHomeStuckAct: int = ParamField(
        byte, "backToHomeStuckAct", NPC_THINK_BackToHomeStuckAct, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(4, "pad3[4]")
    SoundBehaviorId01: int = ParamField(
        int, "soundBehaviorId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId02: int = ParamField(
        int, "soundBehaviorId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId03: int = ParamField(
        int, "soundBehaviorId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId04: int = ParamField(
        int, "soundBehaviorId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId05: int = ParamField(
        int, "soundBehaviorId05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId06: int = ParamField(
        int, "soundBehaviorId06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId07: int = ParamField(
        int, "soundBehaviorId07", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId08: int = ParamField(
        int, "soundBehaviorId08", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOffSpecialEffectId: int = ParamField(
        int, "weaponOffSpecialEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOnSpecialEffectId: int = ParamField(
        int, "weaponOnSpecialEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOffAnimId: int = ParamField(
        int, "weaponOffAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOnAnimId: int = ParamField(
        int, "weaponOnAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SurpriseAnimId: int = ParamField(
        int, "surpriseAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
