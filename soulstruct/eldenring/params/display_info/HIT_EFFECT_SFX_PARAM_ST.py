from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


HIT_EFFECT_SFX_PARAM_ST = {
    "param_type": "HIT_EFFECT_SFX_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "Slash_Normal",
            "Slash: Standard",
            True,
            int,
            'Slash: Standard',
        ),
        ParamFieldInfo(
            "Slash_S",
            "Slash: Small",
            True,
            int,
            'Slash: Small',
        ),
        ParamFieldInfo(
            "Slash_L",
            "Slash: Large",
            True,
            int,
            'Slash: Large',
        ),
        ParamFieldInfo(
            "Slash_Specific1",
            "Slash: Specific 1",
            True,
            int,
            'Slash: Specific 1',
        ),
        ParamFieldInfo(
            "Slash_Specific2",
            "Slash: Specific 2",
            True,
            int,
            'Slash: Specific 2',
        ),
        ParamFieldInfo(
            "Blow_Normal",
            "Batter: Standard",
            True,
            int,
            'Batter: Standard',
        ),
        ParamFieldInfo(
            "Blow_S",
            "Batter: Small",
            True,
            int,
            'Batter: Small',
        ),
        ParamFieldInfo(
            "Blow_L",
            "Batter: Large",
            True,
            int,
            'Batter: Large',
        ),
        ParamFieldInfo(
            "Blow_Specific1",
            "Batter: Specific 1",
            True,
            int,
            'Batter: Specific 1',
        ),
        ParamFieldInfo(
            "Blow_Specific2",
            "Batter: Specific 2",
            True,
            int,
            'Batter: Specific 2',
        ),
        ParamFieldInfo(
            "Thrust_Normal",
            "Piercing: Standard",
            True,
            int,
            'Piercing: Standard',
        ),
        ParamFieldInfo(
            "Thrust_S",
            "Piercing: Small",
            True,
            int,
            'Piercing: Small',
        ),
        ParamFieldInfo(
            "Thrust_L",
            "Piercing: Large",
            True,
            int,
            'Piercing: Large',
        ),
        ParamFieldInfo(
            "Thrust_Specific1",
            "Piercing: Specific 1",
            True,
            int,
            'Piercing: Specific 1',
        ),
        ParamFieldInfo(
            "Thrust_Specific2",
            "Piercing: Specific 2",
            True,
            int,
            'Piercing: Specific 2',
        ),
        ParamFieldInfo(
            "Neutral_Normal",
            "Neutral: Standard",
            True,
            int,
            'Neutral: standard',
        ),
        ParamFieldInfo(
            "Neutral_S",
            "Neutral: Small",
            True,
            int,
            'Neutral: Small',
        ),
        ParamFieldInfo(
            "Neutral_L",
            "Neutral: Large",
            True,
            int,
            'Neutral: Large',
        ),
        ParamFieldInfo(
            "Neutral_Specific1",
            "Neutral: Specific 1",
            True,
            int,
            'Neutral: Specific 1',
        ),
        ParamFieldInfo(
            "Neutral_Specific2",
            "Neutral: Specific 2",
            True,
            int,
            'Neutral: Specific 2',
        ),
    ],
}
