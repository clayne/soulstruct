from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SP_EFFECT_VFX_PARAM_ST = {
    "param_type": "SP_EFFECT_VFX_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "midstSfxId",
            "Midst SFX ID",
            True,
            int,
            'In effect SfxID (-1: invalid)',
        ),
        ParamFieldInfo(
            "midstSeId",
            "Midst SE ID",
            True,
            int,
            'In effect SeID (-1: invalid)',
        ),
        ParamFieldInfo(
            "initSfxId",
            "Start SFX ID",
            True,
            int,
            'SfxID at activation (-1: invalid)',
        ),
        ParamFieldInfo(
            "initSeId",
            "Start SE ID",
            True,
            int,
            'When activated SeID (-1: invalid)',
        ),
        ParamFieldInfo(
            "finishSfxId",
            "End SFX ID",
            True,
            int,
            'SfxID at the time of cancellation (-1: invalid)',
        ),
        ParamFieldInfo(
            "finishSeId",
            "End SE ID",
            True,
            int,
            'SeID at the time of release (-1: invalid)',
        ),
        ParamFieldInfo(
            "camouflageBeginDist",
            "Camouflage - Start Distance",
            True,
            float,
            'It is the camouflage start distance',
        ),
        ParamFieldInfo(
            "camouflageEndDist",
            "Camouflage - End Distance",
            True,
            float,
            'It is the camouflage end distance',
        ),
        ParamFieldInfo(
            "transformProtectorId",
            "Transform - Protector ID",
            True,
            int,
            'Makeover Armor ID (-1: None)',
        ),
        ParamFieldInfo(
            "midstDmyId",
            "Midst Dummy Poly ID",
            True,
            int,
            'In effect Damipoli ID (-1: Root)',
        ),
        ParamFieldInfo(
            "initDmyId",
            "Start Dummy Poly ID",
            True,
            int,
            'Damipoli ID at the time of activation (-1: root)',
        ),
        ParamFieldInfo(
            "finishDmyId",
            "End Dummy Poly ID",
            True,
            int,
            'Damipoli ID at the time of cancellation (-1: root)',
        ),
        ParamFieldInfo(
            "effectType",
            "Effect Type",
            True,
            int,
            'Effect type',
        ),
        ParamFieldInfo(
            "soulParamIdForWepEnchant",
            "Weapon Enchant - Soul Param ID",
            True,
            int,
            'Soul Param ID for Weapon Enchantment (-1: None). Change the applied Phantom Param.',
        ),
        ParamFieldInfo(
            "playCategory",
            "Play Category",
            True,
            int,
            'Controls effect playback due to duplicate effects',
        ),
        ParamFieldInfo(
            "playPriority",
            "Play Priority",
            True,
            int,
            'Set the playback priority when the categories match (lower one has priority)',
        ),
        ParamFieldInfo(
            "existEffectForLarge:1",
            "Large Effect Exists",
            True,
            int,
            'Is there a large effect?',
        ),
        ParamFieldInfo(
            "existEffectForSoul:1",
            "Soul Effect Exists",
            True,
            int,
            'Is there an effect for the soul body?',
        ),
        ParamFieldInfo(
            "effectInvisibleAtCamouflage:1",
            "Camouflage - Invisible while Active",
            True,
            int,
            'Whether to hide the effect when hiding',
        ),
        ParamFieldInfo(
            "useCamouflage:1",
            "Camouflage - Enable",
            True,
            int,
            'Do you hide',
        ),
        ParamFieldInfo(
            "invisibleAtFriendCamouflage:1",
            "Camouflage - Invisible for Friend",
            True,
            int,
            'Is it hidden even by allies when hiding?',
        ),
        ParamFieldInfo(
            "isHideFootEffect_forCamouflage:1",
            "Camouflage - Hide Foot Effect",
            True,
            int,
            'Do you want to turn off the foot effect when hiding?',
        ),
        ParamFieldInfo(
            "halfCamouflage:1",
            "Camouflage - Translucent Appearance",
            True,
            int,
            'Only translucent appearance',
        ),
        ParamFieldInfo(
            "isFullBodyTransformProtectorId:1",
            "Is Full Body Protector ID",
            True,
            int,
            'Is the transformation armor ID for the whole body?',
        ),
        ParamFieldInfo(
            "isInvisibleWeapon:1",
            "Is Invisible Weapon",
            True,
            int,
            'Invisible Weapon for Weapon Enchantment (0: Weapon Show, 1: Weapon Hide)',
        ),
        ParamFieldInfo(
            "isSilence:1",
            "Is Silent",
            True,
            int,
            'Is it silence? (0: No, 1: Yes)',
        ),
        ParamFieldInfo(
            "isMidstFullbody:1",
            "Is Midst SFX Full Body",
            True,
            int,
            'Do you use whole body Damipoli for equipping SFX during effect? Play SFX from torso: 190, head: 191, hands: 192, legs: 193 at 1',
        ),
        ParamFieldInfo(
            "isInitFullbody:1",
            "Is Start SFX Full Body",
            True,
            int,
            'Do you use the whole body Damipoli for equipping SFX during activation? Play SFX from torso: 190, head: 191, hands: 192, legs: 193 at 1',
        ),
        ParamFieldInfo(
            "isFinishFullbody:1",
            "Is End SFX Full Body",
            True,
            int,
            'Do you use the whole body Damipoli for equipping SFX at the time of release? Play SFX from torso: 190, head: 191, hands: 192, legs: 193 at 1',
        ),
        ParamFieldInfo(
            "isVisibleDeadChr:1",
            "Is Visible on Dead Chr",
            True,
            int,
            'If ��, VFX will be displayed even when the corpse is dead.',
        ),
        ParamFieldInfo(
            "isUseOffsetEnchantSfxSize:1",
            "Use Enchant SFX Size to Offset SFX ID",
            True,
            int,
            'Whether to offset the SfxId according to the "enchantment Sfx size" of the weapon para',
        ),
        ParamFieldInfo(
            "pad_1:1",
            "Padding",
            False,
            bit_pad_field(1),
            'Padding',
        ),
        ParamFieldInfo(
            "decalId1",
            "Decal ID [0]",
            True,
            int,
            'Decal ID 1 (-1: invalid)',
        ),
        ParamFieldInfo(
            "decalId2",
            "Decal ID [1]",
            True,
            int,
            'Decal ID 2 (-1: invalid)',
        ),
        ParamFieldInfo(
            "footEffectPriority",
            "Foot Effect Priority",
            True,
            int,
            'Foot effect offset priority (lower is higher)',
        ),
        ParamFieldInfo(
            "footEffectOffset",
            "Foot Effect Offset",
            True,
            int,
            'Amount offset to foot effect ID when this special effect is applied',
        ),
        ParamFieldInfo(
            "traceSfxIdOffsetType",
            "Trace SFX ID Offset Type",
            True,
            int,
            'The offset value applied to the sword flash SFX ID. Used for enchantment and sword trajectory effects',
        ),
        ParamFieldInfo(
            "forceDeceasedType",
            "Force Deceased Type",
            True,
            int,
            'A function that can force the appearance of a character to be alive / dead',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_0",
            "Enchant SFX Start - Dummy Poly ID [0]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_0",
            "Enchant SFX end - Dummy Poly ID [0]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_1",
            "Enchant SFX Start - Dummy Poly ID [1]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_1",
            "Enchant SFX End - Dummy Poly ID [1]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_2",
            "Enchant SFX Start - Dummy Poly ID [2]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_2",
            "Enchant SFX End - Dummy Poly ID [2]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_3",
            "Enchant SFX Start - Dummy Poly ID [3]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_3",
            "Enchant SFX End - Dummy Poly ID [3]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_4",
            "Enchant SFX Start - Dummy Poly ID [4]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_4",
            "Enchant SFX End - Dummy Poly ID [4]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_5",
            "Enchant SFX Start - Dummy Poly ID [5]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_5",
            "Enchant SFX End - Dummy Poly ID [5]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_6",
            "Enchant SFX Start - Dummy Poly ID [6]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_6",
            "Enchant SFX End - Dummy Poly ID [6]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "enchantStartDmyId_7",
            "Enchant SFX Start - Dummy Poly ID [7]",
            True,
            int,
            'Damipoli ID generated at the base of enchantment',
        ),
        ParamFieldInfo(
            "enchantEndDmyId_7",
            "Enchant SFX End - Dummy Poly ID [7]",
            True,
            int,
            'Damipoli ID generated at the tip of the sword at the time of enchantment. -1 If specified, it will be automatically put out to the point where it is a serial number.',
        ),
        ParamFieldInfo(
            "SfxIdOffsetType",
            "SFX ID Offset Type",
            True,
            int,
            'SfxID offset type',
        ),
        ParamFieldInfo(
            "phantomParamOverwriteType",
            "Phantom Param Overwrite Type",
            True,
            int,
            'Forced overwrite type of phantom parameters',
        ),
        ParamFieldInfo(
            "camouflageMinAlpha",
            "Camouflage - Min Alpha",
            True,
            int,
            'Minimum �� value when hiding [%]',
        ),
        ParamFieldInfo(
            "wetAspectType",
            "Wet Aspect Type",
            True,
            int,
            'Generate a wet expression by referring to the wet parameter',
        ),
        ParamFieldInfo(
            "phantomParamOverwriteId",
            "Phantom Param Overwrite ID",
            True,
            int,
            'Forced Id of phantom parameter',
        ),
        ParamFieldInfo(
            "materialParamId",
            "Material Param ID",
            True,
            int,
            'ID0-99 are GS reservation IDs. If ID100 or later is specified, the material extension parameter is referenced (-1: invalid value).',
        ),
        ParamFieldInfo(
            "materialParamInitValue",
            "Material Param - Start Fade",
            True,
            float,
            'The value at the start of the fade of the material parameter. The target is specified by the material parameter ID. If the material parameter ID is -1, do nothing',
        ),
        ParamFieldInfo(
            "materialParamTargetValue",
            "Material Param - End Fade",
            True,
            float,
            'The value at the end of the fade of the material parameter. The target is specified by the material parameter ID. If the material parameter ID is -1, do nothing',
        ),
        ParamFieldInfo(
            "materialParamFadeTime",
            "Material Param - Fade Time",
            True,
            float,
            'Fade time for material parameter values. Gradually reach the target value over this time. If the material parameter ID is -1, do nothing',
        ),
        ParamFieldInfo(
            "footDecalMaterialOffsetOverwriteId",
            "Foot Decal Material Offset Overwrite ID",
            True,
            int,
            'Forcibly rewrite the floor material ID offset of the foot decal (-1 unused)',
        ),
        ParamFieldInfo(
            "pad[14]",
            "Padding",
            False,
            pad_field(14),
            'Padding',
        ),
    ],
}
