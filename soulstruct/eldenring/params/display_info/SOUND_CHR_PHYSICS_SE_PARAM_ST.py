from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SOUND_CHR_PHYSICS_SE_PARAM_ST = {
    "param_type": "SOUND_CHR_PHYSICS_SE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "disableParam_NT:1",
            "Disable Param - Network Test",
            True,
            int,
            'Parameters marked with �� are excluded in the NT version package.',
        ),
        ParamFieldInfo(
            "disableParamReserve1:7",
            "Reserve for package output 1",
            False,
            bit_pad_field(7),
            'Reserve for package output 1',
        ),
        ParamFieldInfo(
            "disableParamReserve2[3]",
            "Reserve for package output 2",
            False,
            pad_field(3),
            'Reserve for package output 2',
        ),
        ParamFieldInfo(
            "ContactLandSeId",
            "Contact Land on Death - SE ID",
            True,
            int,
            'SEID pronounced when contacting the ground after death. (-1: Invalid). SEID category is fixed to c',
        ),
        ParamFieldInfo(
            "ContactLandAddSeId",
            "Contact Land on Death - Additional SE ID",
            True,
            int,
            'Additional SEID (for material) that sounds when it comes into contact with the ground after death. (-1: Invalid). SEID category is fixed to c',
        ),
        ParamFieldInfo(
            "ContactLandPlayNum",
            "Contact Land on Death - Play Count",
            True,
            int,
            'Number of pronunciations when touching the ground after death',
        ),
        ParamFieldInfo(
            "IsEnablePlayCountPerRigid",
            "Enable Play Count per Rigid Body Unit",
            True,
            int,
            'Do you count the number of pronunciations of surface contact after death in rigid body units? (��: Rigid body unit, �~: Character unit)',
        ),
        ParamFieldInfo(
            "pad[3]",
            "pad",
            False,
            pad_field(3),
            '',
        ),
        ParamFieldInfo(
            "ContactLandMinImpuse",
            "Contact Land on Death - Min Impulse",
            True,
            float,
            'Minimum impulse value required for ground contact determination after death',
        ),
        ParamFieldInfo(
            "ContactLandMinSpeed",
            "Contact Land on Death - Min Speed",
            True,
            float,
            'Minimum speed value required for ground contact determination after death',
        ),
        ParamFieldInfo(
            "ContactPlayerSeId",
            "Contact Player on Death - SE ID",
            True,
            int,
            'SEID that sounds when you come into contact with Player after death. (-1: Invalid). SEID category is fixed to c',
        ),
        ParamFieldInfo(
            "ContactPlayerMinImpuse",
            "Contact Player on Death - Min Impulse",
            True,
            float,
            'Minimum impulse value required for Player contact judgment after death',
        ),
        ParamFieldInfo(
            "ContactPlayerMinSpeed",
            "Contact Player on Death - Min Speed",
            True,
            float,
            'Minimum speed value required for Player contact judgment after death',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx0",
            "Contact Check Rigid Index [0]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx1",
            "Contact Check Rigid Index [1]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx2",
            "Contact Check Rigid Index [2]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx3",
            "Contact Check Rigid Index [3]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx4",
            "Contact Check Rigid Index [4]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx5",
            "Contact Check Rigid Index [5]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx6",
            "Contact Check Rigid Index [6]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx7",
            "Contact Check Rigid Index [7]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx8",
            "Contact Check Rigid Index [8]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx9",
            "Contact Check Rigid Index [9]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx10",
            "Contact Check Rigid Index [10]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx11",
            "Contact Check Rigid Index [11]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx12",
            "Contact Check Rigid Index [12]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx13",
            "Contact Check Rigid Index [13]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx14",
            "Contact Check Rigid Index [14]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
        ParamFieldInfo(
            "ContactCheckRigidIdx15",
            "Contact Check Rigid Index [15]",
            True,
            int,
            'Specify the INDEX of the rigid body for contact judgment. Specify only the rigid body to which you want to attach SE',
        ),
    ],
}
