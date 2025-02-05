from __future__ import annotations

__all__ = ["NETWORK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NETWORK_PARAM_ST(ParamRow):
    SignVerticalOffset: float = ParamField(
        float, "signVerticalOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignPosCorrectionRange: float = ParamField(
        float, "maxSignPosCorrectionRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SummonTimeoutTime: float = ParamField(
        float, "summonTimeoutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
    SignPuddleActiveMessageIntervalSec: float = ParamField(
        float, "signPuddleActiveMessageIntervalSec", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideHeight: float = ParamField(
        float, "keyGuideHeight", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignIntervalTime1: float = ParamField(
        float, "reloadSignIntervalTime1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignIntervalTime2: float = ParamField(
        float, "reloadSignIntervalTime2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignTotalCount: int = ParamField(
        uint, "reloadSignTotalCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignCellCount: int = ParamField(
        uint, "reloadSignCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    UpdateSignIntervalTime: float = ParamField(
        float, "updateSignIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveRange: float = ParamField(
        float, "basicExclusiveRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveHeight: float = ParamField(
        float, "basicExclusiveHeight", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PreviewChrWaitingTime: float = ParamField(
        float, "previewChrWaitingTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignVisibleRange: float = ParamField(
        float, "signVisibleRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupHorizontalRange: int = ParamField(
        uint, "cellGroupHorizontalRange", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupTopRange: int = ParamField(
        uint, "cellGroupTopRange", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupBottomRange: int = ParamField(
        uint, "cellGroupBottomRange", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MinWhitePhantomLimitTimeScale: float = ParamField(
        float, "minWhitePhantomLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MinSmallPhantomLimitTimeScale: float = ParamField(
        float, "minSmallPhantomLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteKeywordLimitTimeScale: float = ParamField(
        float, "whiteKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SmallKeywordLimitTimeScale: float = ParamField(
        float, "smallKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackKeywordLimitTimeScale: float = ParamField(
        float, "blackKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DragonKeywordLimitTimeScale: float = ParamField(
        float, "dragonKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SingGetMax: int = ParamField(
        uint, "singGetMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SignDownloadSpan: float = ParamField(
        float, "signDownloadSpan", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignUpdateSpan: float = ParamField(
        float, "signUpdateSpan", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "signPad[4]")
    MaxBreakInTargetListCount: int = ParamField(
        uint, "maxBreakInTargetListCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BreakInRequestIntervalTimeSec: float = ParamField(
        float, "breakInRequestIntervalTimeSec", default=4.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInRequestTimeOutSec: float = ParamField(
        float, "breakInRequestTimeOutSec", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideRange: float = ParamField(
        float, "keyGuideRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadNewSignCellCount: int = ParamField(
        uint, "reloadNewSignCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadRandomSignCellCount: int = ParamField(
        uint, "reloadRandomSignCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignTotalCount: int = ParamField(
        uint, "maxSignTotalCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignCellCount: int = ParamField(
        uint, "maxSignCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxWriteSignCount: int = ParamField(
        uint, "maxWriteSignCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxReadSignCount: int = ParamField(
        uint, "maxReadSignCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignIntervalTime: float = ParamField(
        float, "reloadSignIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTime: int = ParamField(
        uint, "lifeTime", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DownloadSpan: float = ParamField(
        float, "downloadSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DownloadEvaluationSpan: float = ParamField(
        float, "downloadEvaluationSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DeadingGhostStartPosThreshold: float = ParamField(
        float, "deadingGhostStartPosThreshold", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideRangePlayer: float = ParamField(
        float, "keyGuideRangePlayer", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideHeightPlayer: float = ParamField(
        float, "keyGuideHeightPlayer", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RecordDeadingGhostTotalTime: float = ParamField(
        float, "recordDeadingGhostTotalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RecordDeadingGhostMinTime: float = ParamField(
        float, "recordDeadingGhostMinTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    StatueCreatableDistance: float = ParamField(
        float, "statueCreatableDistance", default=80.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadGhostTotalCount: int = ParamField(
        uint, "reloadGhostTotalCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadGhostCellCount: int = ParamField(
        uint, "reloadGhostCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxGhostTotalCount: int = ParamField(
        uint, "maxGhostTotalCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DistanceOfBeginRecordVersus: float = ParamField(
        float, "distanceOfBeginRecordVersus", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DistanceOfEndRecordVersus: float = ParamField(
        float, "distanceOfEndRecordVersus", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    UpdateWanderGhostIntervalTime: float = ParamField(
        float, "updateWanderGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    UpdateVersusGhostIntervalTime: float = ParamField(
        float, "updateVersusGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RecordWanderingGhostTime: float = ParamField(
        float, "recordWanderingGhostTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RecordWanderingGhostMinTime: float = ParamField(
        float, "recordWanderingGhostMinTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    UpdateBonfireGhostIntervalTime: float = ParamField(
        float, "updateBonfireGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayGhostRangeOnView: float = ParamField(
        float, "replayGhostRangeOnView", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayGhostRangeOutView: float = ParamField(
        float, "replayGhostRangeOutView", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfireGhostTime: float = ParamField(
        float, "replayBonfireGhostTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MinBonfireGhostValidRange: float = ParamField(
        float, "minBonfireGhostValidRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxBonfireGhostValidRange: float = ParamField(
        float, "maxBonfireGhostValidRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MinReplayIntervalTime: float = ParamField(
        float, "minReplayIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxReplayIntervalTime: float = ParamField(
        float, "maxReplayIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadGhostIntervalTime: float = ParamField(
        float, "reloadGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfirePhantomParamIdForCodename: int = ParamField(
        int, "replayBonfirePhantomParamIdForCodename", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfireModeRange: float = ParamField(
        float, "replayBonfireModeRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfirePhantomParamId: int = ParamField(
        int, "replayBonfirePhantomParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(4, "ghostpad[4]")
    ReloadVisitListCoolTime: float = ParamField(
        float, "reloadVisitListCoolTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxCoopBlueSummonCount: int = ParamField(
        uint, "maxCoopBlueSummonCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxBellGuardSummonCount: int = ParamField(
        uint, "maxBellGuardSummonCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxVisitListCount: int = ParamField(
        uint, "maxVisitListCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchCoopBlueMin: float = ParamField(
        float, "reloadSearch_CoopBlue_Min", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchCoopBlueMax: float = ParamField(
        float, "reloadSearch_CoopBlue_Max", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchBellGuardMin: float = ParamField(
        float, "reloadSearch_BellGuard_Min", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchBellGuardMax: float = ParamField(
        float, "reloadSearch_BellGuard_Max", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchRatKingMin: float = ParamField(
        float, "reloadSearch_RatKing_Min", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchRatKingMax: float = ParamField(
        float, "reloadSearch_RatKing_Max", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "visitpad00[8]")
    SrttMaxLimit: float = ParamField(
        float, "srttMaxLimit", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    SrttMeanLimit: float = ParamField(
        float, "srttMeanLimit", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    SrttMeanDeviationLimit: float = ParamField(
        float, "srttMeanDeviationLimit", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkPhantomLimitBoostTime: float = ParamField(
        float, "darkPhantomLimitBoostTime", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkPhantomLimitBoostScale: float = ParamField(
        float, "darkPhantomLimitBoostScale", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    MultiplayDisableLifeTime: float = ParamField(
        float, "multiplayDisableLifeTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AbyssMultiplayLimit: int = ParamField(
        byte, "abyssMultiplayLimit", default=10,
        tooltip="TOOLTIP-TODO",
    )
    PhantomWarpMinimumTime: int = ParamField(
        byte, "phantomWarpMinimumTime", default=5,
        tooltip="TOOLTIP-TODO",
    )
    PhantomReturnDelayTime: int = ParamField(
        byte, "phantomReturnDelayTime", default=5,
        tooltip="TOOLTIP-TODO",
    )
    TerminateTimeoutTime: int = ParamField(
        byte, "terminateTimeoutTime", default=30,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointLanDisconnect: int = ParamField(
        ushort, "penaltyPointLanDisconnect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointSignout: int = ParamField(
        ushort, "penaltyPointSignout", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointReboot: int = ParamField(
        ushort, "penaltyPointReboot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointBeginPenalize: int = ParamField(
        ushort, "penaltyPointBeginPenalize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyForgiveItemLimitTime: float = ParamField(
        float, "penaltyForgiveItemLimitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AllAreaSearchRateCoopBlue: int = ParamField(
        byte, "allAreaSearchRate_CoopBlue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AllAreaSearchRateVsBlue: int = ParamField(
        byte, "allAreaSearchRate_VsBlue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AllAreaSearchRateBellGuard: int = ParamField(
        byte, "allAreaSearchRate_BellGuard", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BloodMessageEvalHealRate: int = ParamField(
        byte, "bloodMessageEvalHealRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SmallGoldSuccessHostRewardId: int = ParamField(
        uint, "smallGoldSuccessHostRewardId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DoorInvalidPlayAreaExtents: float = ParamField(
        float, "doorInvalidPlayAreaExtents", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignDisplayMax: int = ParamField(
        byte, "signDisplayMax", default=10,
        tooltip="TOOLTIP-TODO",
    )
    BloodStainDisplayMax: int = ParamField(
        byte, "bloodStainDisplayMax", default=7,
        tooltip="TOOLTIP-TODO",
    )
    BloodMessageDisplayMax: int = ParamField(
        byte, "bloodMessageDisplayMax", default=3,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(9, "pad00[9]")
    _Pad5: bytes = ParamPad(32, "pad10[32]")
    SummonMessageInterval: float = ParamField(
        float, "summonMessageInterval", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HostRegisterUpdateTime: float = ParamField(
        float, "hostRegisterUpdateTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HostTimeOutTime: float = ParamField(
        float, "hostTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestUpdateTime: float = ParamField(
        float, "guestUpdateTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestPlayerNoTimeOutTime: float = ParamField(
        float, "guestPlayerNoTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HostPlayerNoTimeOutTime: float = ParamField(
        float, "hostPlayerNoTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RequestSearchQuickMatchLimit: int = ParamField(
        uint, "requestSearchQuickMatchLimit", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AvatarMatchSearchMax: int = ParamField(
        uint, "AvatarMatchSearchMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyalMatchSearchMin: int = ParamField(
        uint, "BattleRoyalMatchSearchMin", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyalMatchSearchMax: int = ParamField(
        uint, "BattleRoyalMatchSearchMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(8, "pad11[8]")
    VisitorListMax: int = ParamField(
        uint, "VisitorListMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VisitorTimeOutTime: float = ParamField(
        float, "VisitorTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DownloadSpan: float = ParamField(
        float, "DownloadSpan", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VisitorGuestRequestMessageIntervalSec: float = ParamField(
        float, "VisitorGuestRequestMessageIntervalSec", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WanderGhostIntervalLifeTime: float = ParamField(
        float, "wanderGhostIntervalLifeTime", default=40.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad7: bytes = ParamPad(12, "pad13[12]")
    YellowMonkTimeOutTime: float = ParamField(
        float, "YellowMonkTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonkDownloadSpan: float = ParamField(
        float, "YellowMonkDownloadSpan", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonkOverallFlowTimeOutTime: float = ParamField(
        float, "YellowMonkOverallFlowTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad8: bytes = ParamPad(4, "pad14[4]")
    _Pad9: bytes = ParamPad(8, "pad14[8]")
