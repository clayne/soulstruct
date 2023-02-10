__all__ = ["OBJECT_PARAM_ST", "OBJ_ACT_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, DynamicParamFieldInfo, pad_field, bit_pad_field
from soulstruct.bloodborne.params.enums import *
from soulstruct.bloodborne.game_types import *


class DynamicObjActRef(DynamicParamFieldInfo):

    POSSIBLE_TYPES = {GoodParam, SpecialEffectParam}

    def __call__(self, entry) -> ParamFieldInfo:
        n = "2" if self.type_field_name.endswith("2") else "1"
        if entry[self.type_field_name] == OBJACT_SP_QUALIFIED_TYPE.NoCondition:
            return ParamFieldInfo(
                self.name,
                f"NoCondition{n}",
                True,
                int,
                f"No condition type selected.",
            )
        elif entry[self.type_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasGood:
            return ParamFieldInfo(
                self.name,
                f"RequiredGood{n}",
                True,
                GoodParam,
                f"Condition: object action will succeed if user has this good in their inventory (does not "
                "include Bottomless Box).",
            )
        elif entry[self.type_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasSpecialEffect:
            return ParamFieldInfo(
                self.name,
                f"RequiredSpecialEffect{n}",
                True,
                SpecialEffectParam,
                "Condition: object action will succeed if user has this special effect.",
            )
        else:
            return ParamFieldInfo(
                self.name,
                f"UnknownCondition{n}",
                True,
                int,
                "Could not determine success condition ID type (usually HasGood or HasSpecialEffect).",
            )


OBJECT_PARAM_ST = {
    "param_type": "OBJECT_PARAM_ST",
    "file_name": "ObjectParam",
    "nickname": "Objects",
    "fields": [
        ParamFieldInfo(
            "hp",
            "ObjectHP",
            True,
            int,
            "Amount of damage object can take before it is destroyed. (Set to -1 for invulnerability.)",
        ),
        ParamFieldInfo(
            "defense",
            "MinAttackForDamage",
            True,
            int,
            "Minimum attack power required to damage object. Attacks with less power than this will deal no "
            "damage.",
        ),
        ParamFieldInfo(
            "extRefTexId",
            "ExternalTextureID",
            False,
            int,
            "Internal description: 'mAA / mAA_????.tpf (-1: None) (AA: Area number)'.",
        ),
        ParamFieldInfo(
            "materialId",
            "MaterialID",
            True,
            TerrainParam,
            "Treated the same as floor material. (Set to -1 to use default.)",
        ),
        ParamFieldInfo(
            "animBreakIdMax",
            "MaxDestructionAnimationID",
            False,
            int,  # TODO: Animation
            "Upper limit of range of destruction animations, which seem to always start at 0.",
        ),
        ParamFieldInfo(
            "isCamHit:1", "CollidesWithCamera", True, bool, "If True, the camera will collide with this object."
        ),
        ParamFieldInfo(
            "isBreakByPlayerCollide:1",
            "BrokenByPlayerCollision",
            True,
            bool,
            "If True, the player will break the object just by touching it.",
        ),
        ParamFieldInfo(
            "isAnimBreak:1",
            "HasDestructionAnimation",
            True,
            bool,
            "If True, the object will use an animation when destroyed rather than using physics-based destruction.",
        ),
        ParamFieldInfo(
            "isPenetrationBulletHit:1",
            "HitByPiercingBullets",
            True,
            bool,
            "If True, the object can be damaged by Bullets with target-piercing enabled.",
        ),
        ParamFieldInfo(
            "isChrHit:1",
            "CharacterCollision",
            True,
            bool,
            "If False, characters will pass through the object (e.g. branches).",
        ),
        ParamFieldInfo(
            "isAttackBacklash:1",
            "DeflectsAttacks",
            True,
            bool,
            "If True, attacks will bounce off the object as though it were a wall.",
        ),
        ParamFieldInfo(
            "isDisableBreakForFirstAppear:1",
            "CannotSpawnBroken",
            True,
            bool,
            "If True, the object cannot be destroyed when the player first spawns.",
        ),
        ParamFieldInfo("isLadder:1", "IsLadder", True, bool, "Object is a ladder."),
        ParamFieldInfo(
            "isAnimPauseOnRemoPlay:1",
            "StopAnimationDuringCutscenes",
            True,
            bool,
            "If True, object animation will not play in cutscenes.",
        ),
        ParamFieldInfo(
            "isDamageNoHit:1",
            "PreventAllDamage",
            True,
            bool,
            "If True, all damage to the object will be prevented. (Not sure if this is the same effet as settings "
            "its HP to -1.)",
        ),
        ParamFieldInfo("isMoveObj:1", "IsMovingObject", True, bool, "If True, this object can move."),
        ParamFieldInfo("pad_1:5", "Pad1", False, bit_pad_field(5), "Null padding."),
        # TODO: LOD type.
        ParamFieldInfo("defaultLodParamId", "DefaultLOD", True, int, "Default LOD (level of default) parameter."),
        ParamFieldInfo(
            "breakSfxId",
            "DestructionSoundEffect",
            True,
            SFXSound,
            "Sound effect played upon destruction. (Set to -1 to use default value, which is apparently 80.)",
        ),
        ParamFieldInfo("navimeshFlag", "NavmeshFlag", True, OBJECT_NAVIMESH_FLAG, ""),
        ParamFieldInfo("pad_2[1]", "Pad", False, pad_field(1), "Null padding."),
        ParamFieldInfo("paintRenderTargetSize", "PaintRenderTargetSize", True, int, ""),
        ParamFieldInfo("breakAiSoundId", "BreakAISoundID", True, int, ""),  # TODO: AI Sound param type
        ParamFieldInfo("pad_3[8]", "Pad", False, pad_field(8), "Null padding."),
    ],
}


OBJ_ACT_PARAM_ST = {
    "param_type": "OBJ_ACT_PARAM_ST",
    "file_name": "ObjActParam",
    "nickname": "ObjectActivations",
    "fields": [
        ParamFieldInfo(
            "actionEnableMsgId",
            "PromptMessage",
            True,
            EventText,
            "Message displayed in dialog box that prompts action (e.g. 'Open').",
        ),
        ParamFieldInfo(
            "actionFailedMsgId",
            "FailureMessage",
            True,
            EventText,
            "Message displayed in dialog box upon failed action (e.g. 'It's locked').",
        ),
        ParamFieldInfo(
            "spQualifiedPassEventFlag",
            "FlagForAutomaticSuccess",
            True,
            Flag,
            "Action will always be successful if this flag is enabled.",
        ),
        ParamFieldInfo(
            "validDist",
            "MaxActionDistance",
            True,
            int,
            "Maximum distance from action model point at which the object action will be prompted.",
        ),
        ParamFieldInfo(
            "playerAnimId",
            "PlayerActionAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by a player character when they successfully activate the object.",
        ),
        ParamFieldInfo(
            "chrAnimId",
            "NonPlayerActionAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by a non-player character when they successfully activate the object.",
        ),
        ParamFieldInfo(
            "spQualifiedType",
            "SuccessCondition1Type",
            True,
            OBJACT_SP_QUALIFIED_TYPE,
            "Type of first success condition.",
        ),
        DynamicObjActRef("spQualifiedId", "spQualifiedType"),
        ParamFieldInfo(
            "spQualifiedType2",
            "SuccessCondition2Type",
            True,
            OBJACT_SP_QUALIFIED_TYPE,
            "Type of second success condition.",
        ),
        DynamicObjActRef("spQualifiedId2", "spQualifiedType2"),
        ParamFieldInfo(
            "objDummyId",
            "ObjectActionModelPoint",
            True,
            int,
            "Model point that specifies where the action occurs on the object (for snapping the player and "
            "distance check).",
        ),
        ParamFieldInfo("pad0[1]", "Pad", False, pad_field(1), ""),
        ParamFieldInfo(
            "objAnimId",
            "ObjectActionAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by the object when it is successfully activated.",
        ),
        ParamFieldInfo(
            "validPlayerAngle",
            "MaxPlayerAngle",
            True,
            int,
            "Maximum angle between the character's forward direction and the direction to the object action point "
            "for the action prompt to appear.",
        ),
        ParamFieldInfo(
            "validObjAngle",
            "MaxObjectAngle",
            True,
            int,
            "Maximum angle between the object's forward direction and the direction to the player for the action "
            "prompt to appear.",
        ),
        ParamFieldInfo(
            "chrSorbType",
            "CharacterSnapType",
            True,
            OBJACT_CHR_SORB_TYPE,
            "Type of method used to snap the character to the object before animations are played.",
        ),
        ParamFieldInfo(
            "eventKickTiming",
            "EventTriggerDelay",
            True,
            int,
            "I believe this is the delay between successful object activation and the outgoing 'success' trigger "
            "used by game events.",
        ),
        ParamFieldInfo("pad1[2]", "Pad1", False, pad_field(2), "Null padding."),
        ParamFieldInfo("actionButtonParamId", "ActionButtonParamID", True, int, ""),  # TODO: param type
        ParamFieldInfo("actionSuccessMsgId", "ActionSuccessMessageID", True, EventText, ""),
    ],
}
