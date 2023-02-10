from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


NETWORK_PARAM_ST = {
    "param_type": "NETWORK_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "signVerticalOffset",
            "Common - Sign Height Offset",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "maxSignPosCorrectionRange",
            "Common - Max Sign Position Correction Range",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "summonTimeoutTime",
            "Common - Summon Timeout Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "pad[4]",
            "reserve",
            False,
            pad_field(4),
            '',
        ),
        ParamFieldInfo(
            "signPuddleActiveMessageIntervalSec",
            "Summon Sign - Sign Puddle Active Message Interval",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "keyGuideHeight",
            "Bloodstain - Key Guide Height",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSignIntervalTime1",
            "Summon Sign - Reload Sign Interval Time [1]",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSignIntervalTime2",
            "Summon Sign - Reload Sign Interval Time [2]",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSignTotalCount",
            "Bloodstain - Reload Sign Total Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "reloadSignCellCount",
            "Bloodstain - Reload Sign Cell Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "updateSignIntervalTime",
            "Summon Sign - Update Sign Interval Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "basicExclusiveRange",
            "Bloodstain - Basic Exclusive Range",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "basicExclusiveHeight",
            "Bloodstain - Basic Exclusive Height",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "previewChrWaitingTime",
            "Summon Sign - Preview Chr Waiting Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "signVisibleRange",
            "Bloodstain - Sign Visible Range",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "cellGroupHorizontalRange",
            "Ghost - Cell Group Horizontal Range",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "cellGroupTopRange",
            "Ghost - Cell Group Top Range",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "cellGroupBottomRange",
            "Bloodstain - Cell Group Bottom Range",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "minWhitePhantomLimitTimeScale",
            "Summon Sign - Min White Phantom Limit Time Scale",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "minSmallPhantomLimitTimeScale",
            "Summon Sign - Min Small Phantom Limit Time Scale",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "whiteKeywordLimitTimeScale",
            "Summon Sign - White Keyword Limit Time Scale",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "smallKeywordLimitTimeScale",
            "Summon Sign - Small Keyword Limit Time Scale",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "blackKeywordLimitTimeScale",
            "Summon Sign - Black Keyword Limit Time Scale",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "dragonKeywordLimitTimeScale",
            "Summon Sign - Dragon Keyword Limit Time Scale",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "singGetMax",
            "Summon Sign - Sign Get Max",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "signDownloadSpan",
            "Summon Sign - Sign Download Span",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "signUpdateSpan",
            "Summon Sign - Sign Update Span",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "signPad[4]",
            "reserve",
            False,
            pad_field(4),
            '',
        ),
        ParamFieldInfo(
            "maxBreakInTargetListCount",
            "Intrusion - Max Intruder List Count",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "breakInRequestIntervalTimeSec",
            "Intrusion - Intruder Request Interval Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "breakInRequestTimeOutSec",
            "Intrusion - Intruder Request Timeout",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "keyGuideRange",
            "Blood Message - Key Guide Horionztal Range",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadNewSignCellCount",
            "Blood Message - Reload New Sign Cell Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "reloadRandomSignCellCount",
            "Blood Message - Reload Random Sign Cell Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "maxSignTotalCount",
            "Bloodstain - Max Sign Total Count",
            True,
            int,
            'Actually u16 is enough',
        ),
        ParamFieldInfo(
            "maxSignCellCount",
            "Bloodstain - Max Sign Cell Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "maxWriteSignCount",
            "Blood Message - Max Write Sign Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "maxReadSignCount",
            "Blood Message - Max Read Sign Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "reloadSignIntervalTime",
            "Bloodstain - Reload Sign Interval Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "lifeTime",
            "Bloodstain - Lifetime",
            True,
            int,
            'Actually u16 is enough',
        ),
        ParamFieldInfo(
            "downloadSpan",
            "Bloodstain - Download Span",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "downloadEvaluationSpan",
            "Blood Message - Download Evaluation Span",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "deadingGhostStartPosThreshold",
            "Bloodstain - Dead Ghost Start Position Threshold",
            True,
            float,
            'If the distance between the bloodstain position and the illusion start position is farther than this value, the server will not be registered.',
        ),
        ParamFieldInfo(
            "keyGuideRangePlayer",
            "Bloodstain - Key Guide Range Player",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "keyGuideHeightPlayer",
            "Bloodstain - Key Guide Height Player",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "recordDeadingGhostTotalTime",
            "Bloodstain - Record Dead Ghost Total Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "recordDeadingGhostMinTime",
            "Bloodstain - Record Dead Ghost Min Time",
            True,
            float,
            'Death illusions less than this recording time will not register the server',
        ),
        ParamFieldInfo(
            "statueCreatableDistance",
            "Bloodstain - Statue Creatable Distance",
            True,
            float,
            'For open fields. When a stone statue is generated, it can be generated if the distance between the PC and the generation position is greater than or equal to this value.',
        ),
        ParamFieldInfo(
            "reloadGhostTotalCount",
            "Ghost - Reload Ghost Total Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "reloadGhostCellCount",
            "Ghost - Reload Ghost Cell Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "maxGhostTotalCount",
            "Ghost - Max Ghost Total Count",
            True,
            int,
            'Actually u16 is enough',
        ),
        ParamFieldInfo(
            "distanceOfBeginRecordVersus",
            "Ghost - Begin Record Distance (Versus)",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "distanceOfEndRecordVersus",
            "Ghost - End Record Distance (Versus)",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "updateWanderGhostIntervalTime",
            "Ghost - Update Wandering Ghost Interval Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "updateVersusGhostIntervalTime",
            "Ghost - Update Versus Ghost Interval Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "recordWanderingGhostTime",
            "Ghost - Record Wandering Ghost Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "recordWanderingGhostMinTime",
            "Ghost - Record Wandering Ghost Min Time",
            True,
            float,
            'Wandering illusions less than this recording time do not register the server',
        ),
        ParamFieldInfo(
            "updateBonfireGhostIntervalTime",
            "Ghost - Update Bonfire Ghost Interval Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "replayGhostRangeOnView",
            "Ghost - Replay Ghost Range On View",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "replayGhostRangeOutView",
            "Ghost - Replay Ghost Range Out View",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "replayBonfireGhostTime",
            "Ghost - Replay Bonfire Ghost Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "minBonfireGhostValidRange",
            "Ghost - Bonfire Ghost Min Valid Range",
            True,
            float,
            'Do not place bonfire illusions less than this distance from the bonfire',
        ),
        ParamFieldInfo(
            "maxBonfireGhostValidRange",
            "Ghost - Bonfire Ghost Max Valid Range",
            True,
            float,
            'Do not place bonfire illusions beyond this distance from the bonfire',
        ),
        ParamFieldInfo(
            "minReplayIntervalTime",
            "Ghost - Replay Interval Min Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "maxReplayIntervalTime",
            "Ghost - Replay Interval Max Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadGhostIntervalTime",
            "Ghost - Reload Ghost Interval Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "replayBonfirePhantomParamIdForCodename",
            "Ghost - Replay Bonfire Phantom Param ID (CodeDisplayName)",
            True,
            int,
            'Phantom bonfire mode phantom parameter ID used when codename matches',
        ),
        ParamFieldInfo(
            "replayBonfireModeRange",
            "Ghost - Replay Bonfire Mode Range",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "replayBonfirePhantomParamId",
            "Ghost - Replay Bonfire Phantom Param ID",
            True,
            int,
            'Phantom bonfire mode phantom parameter ID',
        ),
        ParamFieldInfo(
            "ghostpad[4]",
            "reserve",
            False,
            pad_field(4),
            '',
        ),
        ParamFieldInfo(
            "reloadVisitListCoolTime",
            "Visit - Reload Visit List Cool time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "maxCoopBlueSummonCount",
            "Visit - Max Coop Blue Summon Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "maxBellGuardSummonCount",
            "Visit - Max Bell Guard Summon Count",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "maxVisitListCount",
            "Visit - Max Visit List Count",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "reloadSearch_CoopBlue_Min",
            "Visit - Reload Search - Coop Blue - Min",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSearch_CoopBlue_Max",
            "Visit - Reload Search - Coop Blue - Max",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSearch_BellGuard_Min",
            "Visit - Reload Search - Bell Guard - Min",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSearch_BellGuard_Max",
            "Visit - Reload Search - Bell Guard - Max",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSearch_RatKing_Min",
            "Visit - Reload Search - Rat King - Min",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "reloadSearch_RatKing_Max",
            "Visit - Reload Search - Rat King - Max",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "visitpad00[8]",
            "reserve",
            False,
            pad_field(8),
            '',
        ),
        ParamFieldInfo(
            "srttMaxLimit",
            "Extra - SSRT Max Limit",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "srttMeanLimit",
            "Extra - SSRT Mean Limit",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "srttMeanDeviationLimit",
            "Extra - SSRT Mean Deviation Limit",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "darkPhantomLimitBoostTime",
            "Extra - Dark Phantom Limit Boost Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "darkPhantomLimitBoostScale",
            "Extra - Dark Phantom Limit Boost Scale",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "multiplayDisableLifeTime",
            "Extra - Multiplayer Disable Lifetime",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "abyssMultiplayLimit",
            "Extra - Abyss Multiplayer Limit",
            True,
            int,
            'The number of times the abyss spirit enters the host in the abyss area',
        ),
        ParamFieldInfo(
            "phantomWarpMinimumTime",
            "Extra - Phantom Warp Minimum Time",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "phantomReturnDelayTime",
            "Extra - Phantom Return Delay Time",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "terminateTimeoutTime",
            "Extra - Terminate Timeout Time",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "penaltyPointLanDisconnect",
            "Extra - Penalty Point LAN Disconnet",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "penaltyPointSignout",
            "Extra - Penalty Point Signout",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "penaltyPointReboot",
            "Extra - Penalty Point Reboot",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "penaltyPointBeginPenalize",
            "Extra - Penalty Point Begin Penalize",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "penaltyForgiveItemLimitTime",
            "Extra - Penalty Forgive Item Limit Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "allAreaSearchRate_CoopBlue",
            "Extra - All Area Search Rate - Coop Blue",
            True,
            int,
            'Percentage of searching for intrusion targets from all areas (%)',
        ),
        ParamFieldInfo(
            "allAreaSearchRate_VsBlue",
            "Extra - All Area Search Rate - Vs. Coop Blue",
            True,
            int,
            'Percentage of searching for intrusion targets from all areas (%)',
        ),
        ParamFieldInfo(
            "allAreaSearchRate_BellGuard",
            "Extra - All Area Search Rate - Bell Guard",
            True,
            int,
            'Percentage of searching for intrusion targets from all areas (%)',
        ),
        ParamFieldInfo(
            "bloodMessageEvalHealRate",
            "Extra - Blood Message Eval Heal Rate",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "smallGoldSuccessHostRewardId",
            "Extra - Small Gold Success Host Reward ID",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "doorInvalidPlayAreaExtents",
            "Extra - Door Invalid Play Area Extents",
            True,
            float,
            "The area around the black door that separates the multiplayer area is set to the systematically invalid play area (-1). At that time, make the invalid area thicker with this parameter on the thinner side of the OBJ's bounding box with a black door.",
        ),
        ParamFieldInfo(
            "signDisplayMax",
            "Extra - Sign Display Max",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "bloodStainDisplayMax",
            "Extra - Bloodstain Display Max",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "bloodMessageDisplayMax",
            "Extra - Blood Message Display Max",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "pad00[9]",
            "reserve",
            False,
            pad_field(9),
            '',
        ),
        ParamFieldInfo(
            "pad10[32]",
            "reserve",
            False,
            pad_field(32),
            '',
        ),
        ParamFieldInfo(
            "summonMessageInterval",
            "Quick Match - Summon Message Interval",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "hostRegisterUpdateTime",
            "Quick Match - Host Register Update Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "hostTimeOutTime",
            "Quick Match - Host Time Out Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "guestUpdateTime",
            "Quick Match - Guest Update Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "guestPlayerNoTimeOutTime",
            "Quick Match - Guest Player No Time Out Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "hostPlayerNoTimeOutTime",
            "Quick Match - Host Player No Time Out Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "requestSearchQuickMatchLimit",
            "Quick Match - Request Search Quick Match Limit",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "AvatarMatchSearchMax",
            "Quick Match - Avatar Match Search Max",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "BattleRoyalMatchSearchMin",
            "Quick Match - Battle Royale Match Search Min",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "BattleRoyalMatchSearchMax",
            "Quick Match - Battle Royale Match Search Max",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "pad11[8]",
            "reserve",
            False,
            pad_field(8),
            '',
        ),
        ParamFieldInfo(
            "VisitorListMax",
            "Visitor - Visitor List Max",
            True,
            int,
            'Actually u8 is enough',
        ),
        ParamFieldInfo(
            "VisitorTimeOutTime",
            "Visitor - Visitor Time Out Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "DownloadSpan",
            "Visitor - Download Span",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "VisitorGuestRequestMessageIntervalSec",
            "Visitor - Visitor Guest Request Message Interval",
            True,
            float,
            'Display interval [seconds] of messages sent by visiting guests while searching for a destination',
        ),
        ParamFieldInfo(
            "wanderGhostIntervalLifeTime",
            "Ghost Addition - Wandering Ghost Interval Lifetime",
            True,
            float,
            'Wandering illusion life',
        ),
        ParamFieldInfo(
            "pad13[12]",
            "reserve",
            False,
            pad_field(12),
            'reserve',
        ),
        ParamFieldInfo(
            "YellowMonkTimeOutTime",
            "Yellow Monk - Yellow Monk Timeout Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "YellowMonkDownloadSpan",
            "Yellow Monk - Yellow Monk Download Span",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "YellowMonkOverallFlowTimeOutTime",
            "Yellow Monk - Yellow Monk Overall Flow Time Out Time",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "pad14[4]",
            "reserve",
            False,
            pad_field(4),
            '',
        ),
        ParamFieldInfo(
            "pad14[8]",
            "reserve",
            False,
            pad_field(8),
            '',
        ),
    ],
}
