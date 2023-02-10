from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MISSILE_PARAM_ST = {
    "param_type": "MISSILE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "FFXID",
            "FFXID",
            True,
            int,
            'ID on the FFX editor',
        ),
        ParamFieldInfo(
            "LifeTime",
            "Survival time [frame]",
            True,
            int,
            'Survival time.',
        ),
        ParamFieldInfo(
            "HitSphereRadius",
            "Hit ball radius [cm]",
            True,
            int,
            'Hit ball radius. Unit cm',
        ),
        ParamFieldInfo(
            "HitDamage",
            "Landing damage",
            True,
            int,
            'Amount of damage at the time of landing',
        ),
        ParamFieldInfo(
            "reserve0[6]",
            "reserve",
            False,
            pad_field(6),
            '',
        ),
        ParamFieldInfo(
            "InitVelocity",
            "Initial speed [m / s]",
            True,
            float,
            'Initial speed [m / s]',
        ),
        ParamFieldInfo(
            "distance",
            "Range distance",
            True,
            float,
            'Range distance',
        ),
        ParamFieldInfo(
            "gravityInRange",
            "Gravity within range",
            True,
            float,
            'Gravity within range',
        ),
        ParamFieldInfo(
            "gravityOutRange",
            "Out-of-range gravity",
            True,
            float,
            'Out-of-range gravity',
        ),
        ParamFieldInfo(
            "mp",
            "MP consumption",
            True,
            int,
            'MP consumption',
        ),
        ParamFieldInfo(
            "accelInRange",
            "Acceleration within range",
            True,
            float,
            'Acceleration within range',
        ),
        ParamFieldInfo(
            "accelOutRange",
            "Out-of-range acceleration",
            True,
            float,
            'Out-of-range acceleration',
        ),
        ParamFieldInfo(
            "reserve1[20]",
            "reserve",
            False,
            pad_field(20),
            '',
        ),
        ParamFieldInfo(
            "HitMissileID",
            "Landing ID",
            True,
            int,
            'Landing ID',
        ),
        ParamFieldInfo(
            "DiedNaturaly",
            "Will you die at the end of your life?",
            True,
            int,
            'Will it use up its life without dying even if it lands?',
        ),
        ParamFieldInfo(
            "ExplosionDie",
            "Will it land when the life has expired?",
            True,
            int,
            'Will it land when the life has expired?',
        ),
        ParamFieldInfo(
            "behaviorId",
            "Action ID on hit",
            True,
            int,
            'Action ID given to the opponent when doing damage',
        ),
        ParamFieldInfo(
            "reserve_last[56]",
            "reserve",
            False,
            pad_field(56),
            '',
        ),
    ],
}
