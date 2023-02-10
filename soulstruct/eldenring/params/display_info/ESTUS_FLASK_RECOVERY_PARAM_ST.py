from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


ESTUS_FLASK_RECOVERY_PARAM_ST = {
    "param_type": "ESTUS_FLASK_RECOVERY_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "host",
            "Host",
            True,
            int,
            'Number of host est recovery',
        ),
        ParamFieldInfo(
            "invadeOrb_None",
            "Invasion Orb - None",
            True,
            int,
            'The number of est recovery of the power of the orb whose invasion route is',
        ),
        ParamFieldInfo(
            "invadeOrb_Umbasa",
            "Invasion Orb - Gold",
            True,
            int,
            'The number of est recovery of the power of the orb whose invasion route is',
        ),
        ParamFieldInfo(
            "invadeOrb_Berserker",
            "Invasion Orb - Berserker",
            True,
            int,
            'The number of est recovery of the power of the orb whose invasion route is',
        ),
        ParamFieldInfo(
            "invadeOrb_Sinners",
            "Invasion Orb - Sinner",
            True,
            int,
            'The number of est recovery of the power of the orb whose invasion route is',
        ),
        ParamFieldInfo(
            "invadeSign_None",
            "Invasion Sign - None",
            True,
            int,
            'The number of est recovery of the power whose invasion route is a sign',
        ),
        ParamFieldInfo(
            "invadeSign_Umbasa",
            "Invasion Sign - Gold",
            True,
            int,
            'The number of est recovery of the power whose invasion route is a sign',
        ),
        ParamFieldInfo(
            "invadeSign_Berserker",
            "Invasion Sign - Berserker",
            True,
            int,
            'The number of est recovery of the power whose invasion route is a sign',
        ),
        ParamFieldInfo(
            "invadeSign_Sinners",
            "Invasion Sign - Sinner",
            True,
            int,
            'The number of est recovery of the power whose invasion route is a sign',
        ),
        ParamFieldInfo(
            "invadeRing_Sinners",
            "Invasion Ring - Sinner",
            True,
            int,
            'The number of est recovery of the power of the ring whose invasion route is',
        ),
        ParamFieldInfo(
            "invadeRing_Rosalia",
            "Invasion Ring - Rosalia",
            True,
            int,
            'The number of est recovery of the power of the ring whose invasion route is',
        ),
        ParamFieldInfo(
            "invadeRing_Forest",
            "Invasion Ring - Forest",
            True,
            int,
            'The number of est recovery of the power of the ring whose invasion route is',
        ),
        ParamFieldInfo(
            "coopSign_None",
            "Coop Sign - None",
            True,
            int,
            'The number of est recovery of the power whose cooperation route is a sign',
        ),
        ParamFieldInfo(
            "coopSign_Umbasa",
            "Coop Sign - Gold",
            True,
            int,
            'The number of est recovery of the power whose cooperation route is a sign',
        ),
        ParamFieldInfo(
            "coopSign_Berserker",
            "Coop Sign - Berserker",
            True,
            int,
            'The number of est recovery of the power whose cooperation route is a sign',
        ),
        ParamFieldInfo(
            "coopSign_Sinners",
            "Coop Sign - Sinner",
            True,
            int,
            'The number of est recovery of the power whose cooperation route is a sign',
        ),
        ParamFieldInfo(
            "coopRing_RedHunter",
            "Coop Sign - Red Hunter",
            True,
            int,
            'Cooperation route is the number of est recovery of the power of the ring',
        ),
        ParamFieldInfo(
            "invadeRing_Anor",
            "Invasion Ring - Darkmoon Blade",
            True,
            int,
            'The number of est recovery of the power of the ring whose invasion route is',
        ),
        ParamFieldInfo(
            "paramReplaceRate",
            "Replacement Rate",
            True,
            int,
            'Recovery number Parameter replacement rate',
        ),
        ParamFieldInfo(
            "paramReplaceId",
            "Replace ID",
            True,
            int,
            'Recovery number Parameter replacement destination ID',
        ),
        ParamFieldInfo(
            "pad[8]",
            "pad",
            False,
            pad_field(8),
            '',
        ),
    ],
}
