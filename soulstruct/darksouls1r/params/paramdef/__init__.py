"""NOTE: Almost all identical to PTDE. Three new types and one new Weapon field."""
from __future__ import annotations

__all__ = [
    "ParamDef",
    "ParamDefBND",

    "AI_STANDARD_INFO_BANK",
    "ATK_PARAM_ST",
    "BEHAVIOR_PARAM_ST",
    "BULLET_PARAM_ST",
    "CACL_CORRECT_GRAPH_ST",
    "CHARACTER_INIT_PARAM",
    "DOF_BANK",
    "ENEMY_STANDARD_INFO_BANK",
    "ENV_LIGHT_TEX_BANK",
    "EQUIP_MTRL_SET_PARAM_ST",
    "EQUIP_PARAM_ACCESSORY_ST",
    "EQUIP_PARAM_GOODS_ST",
    "EQUIP_PARAM_PROTECTOR_ST",
    "EQUIP_PARAM_WEAPON_ST",  # updated (barely) in DSR
    "FACE_PARAM_ST",
    "FOG_BANK",
    "GAME_AREA_PARAM_ST",
    "HIT_MTRL_PARAM_ST",
    "ITEMLOT_PARAM_ST",
    "KNOCKBACK_PARAM_ST",
    "LENS_FLARE_BANK",
    "LENS_FLARE_EX_BANK",
    "LIGHT_BANK",
    "LIGHT_SCATTERING_BANK",
    "LOCK_CAM_PARAM_ST",
    "LOD_BANK",
    "MAGIC_PARAM_ST",
    "MENU_PARAM_COLOR_TABLE_ST",
    "MOVE_PARAM_ST",
    "NPC_PARAM_ST",
    "NPC_THINK_PARAM_ST",
    "OBJECT_PARAM_ST",
    "OBJ_ACT_PARAM_ST",
    "POINT_LIGHT_BANK",
    "QWC_CHANGE_PARAM_ST",
    "QWC_JUDGE_PARAM_ST",
    "RAGDOLL_PARAM_ST",
    "REINFORCE_PARAM_PROTECTOR_ST",
    "REINFORCE_PARAM_WEAPON_ST",
    "SHADOW_BANK",
    "SHOP_LINEUP_PARAM",
    "SKELETON_PARAM_ST",
    "SP_EFFECT_PARAM_ST",
    "SP_EFFECT_VFX_PARAM_ST",
    "TALK_PARAM_ST",
    "THROW_INFO_BANK",
    "TONE_CORRECT_BANK",
    "TONE_MAP_BANK",

    # New in DSR:
    "COOL_TIME_PARAM_ST",
    "LEVELSYNC_PARAM_ST",
    "WHITE_COOL_TIME_PARAM_ST",

]

from soulstruct.darksouls1ptde.params.paramdef import *
from .core import *  # override PTDE imports

# NEW
from .COOL_TIME_PARAM_ST import COOL_TIME_PARAM_ST
from .LEVELSYNC_PARAM_ST import LEVELSYNC_PARAM_ST
from .WHITE_COOL_TIME_PARAM_ST import WHITE_COOL_TIME_PARAM_ST

# UPDATED
from .EQUIP_PARAM_GOODS_ST import EQUIP_PARAM_GOODS_ST
from .EQUIP_PARAM_WEAPON_ST import EQUIP_PARAM_WEAPON_ST
from .REINFORCE_PARAM_WEAPON_ST import REINFORCE_PARAM_WEAPON_ST
from .TONE_CORRECT_BANK import TONE_CORRECT_BANK
from .TONE_MAP_BANK import TONE_MAP_BANK
