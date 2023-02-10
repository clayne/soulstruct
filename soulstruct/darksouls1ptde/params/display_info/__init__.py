"""Imports all names from all param categories (loosely sorted into scripts here)."""
from __future__ import annotations

__all__ = [
    "ATK_PARAM_ST",
    "BEHAVIOR_PARAM_ST",
    "BULLET_PARAM_ST",
    "CACL_CORRECT_GRAPH_ST",
    "CHARACTER_INIT_PARAM",
    "DOF_BANK",
    # "ENV_LIGHT_TEX_BANK",
    "EQUIP_MTRL_SET_PARAM_ST",
    "EQUIP_PARAM_ACCESSORY_ST",
    "EQUIP_PARAM_GOODS_ST",
    "EQUIP_PARAM_PROTECTOR_ST",
    "EQUIP_PARAM_WEAPON_ST",
    "FACE_PARAM_ST",
    "FOG_BANK",
    "GAME_AREA_PARAM_ST",
    "HIT_MTRL_PARAM_ST",
    "ITEMLOT_PARAM_ST",
    "LENS_FLARE_BANK",
    "LENS_FLARE_EX_BANK",
    "LIGHT_BANK",
    "LIGHT_SCATTERING_BANK",
    "LOCK_CAM_PARAM_ST",
    # "LOD_BANK",
    "MAGIC_PARAM_ST",
    "MENU_PARAM_COLOR_TABLE_ST",
    "MOVE_PARAM_ST",
    "NPC_PARAM_ST",
    "NPC_THINK_PARAM_ST",
    "OBJECT_PARAM_ST",
    "OBJ_ACT_PARAM_ST",
    "POINT_LIGHT_BANK",
    "REINFORCE_PARAM_PROTECTOR_ST",
    "REINFORCE_PARAM_WEAPON_ST",
    "SHADOW_BANK",
    "SHOP_LINEUP_PARAM",
    "SP_EFFECT_PARAM_ST",
    "SP_EFFECT_VFX_PARAM_ST",
    "TALK_PARAM_ST",
    "THROW_INFO_BANK",
    "TONE_CORRECT_BANK",
    "TONE_MAP_BANK",
]

import typing as tp

from .ATK_PARAM_ST import ATK_PARAM_ST
from .BEHAVIOR_PARAM_ST import BEHAVIOR_PARAM_ST
from .BULLET_PARAM_ST import BULLET_PARAM_ST
from .CACL_CORRECT_GRAPH_ST import CACL_CORRECT_GRAPH_ST
from .CHARACTER_INIT_PARAM import CHARACTER_INIT_PARAM
from .DOF_BANK import DOF_BANK
# from .ENV_LIGHT_TEX_BANK import ENV_LIGHT_TEX_BANK
from .EQUIP_MTRL_SET_PARAM_ST import EQUIP_MTRL_SET_PARAM_ST
from .EQUIP_PARAM_ACCESSORY_ST import EQUIP_PARAM_ACCESSORY_ST
from .EQUIP_PARAM_GOODS_ST import EQUIP_PARAM_GOODS_ST
from .EQUIP_PARAM_PROTECTOR_ST import EQUIP_PARAM_PROTECTOR_ST
from .EQUIP_PARAM_WEAPON_ST import EQUIP_PARAM_WEAPON_ST
from .FACE_PARAM_ST import FACE_PARAM_ST
from .FOG_BANK import FOG_BANK
from .GAME_AREA_PARAM_ST import GAME_AREA_PARAM_ST
from .HIT_MTRL_PARAM_ST import HIT_MTRL_PARAM_ST
from .ITEMLOT_PARAM_ST import ITEMLOT_PARAM_ST
from .LENS_FLARE_BANK import LENS_FLARE_BANK
from .LENS_FLARE_EX_BANK import LENS_FLARE_EX_BANK
from .LIGHT_BANK import LIGHT_BANK
from .LIGHT_SCATTERING_BANK import LIGHT_SCATTERING_BANK
from .LOCK_CAM_PARAM_ST import LOCK_CAM_PARAM_ST
# from .LOD_BANK import LOD_BANK
from .MAGIC_PARAM_ST import MAGIC_PARAM_ST
from .MENU_PARAM_COLOR_TABLE_ST import MENU_PARAM_COLOR_TABLE_ST
from .MOVE_PARAM_ST import MOVE_PARAM_ST
from .NPC_PARAM_ST import NPC_PARAM_ST
from .NPC_THINK_PARAM_ST import NPC_THINK_PARAM_ST
from .OBJECT_PARAM_ST import OBJECT_PARAM_ST
from .OBJ_ACT_PARAM_ST import OBJ_ACT_PARAM_ST
from .POINT_LIGHT_BANK import POINT_LIGHT_BANK
from .REINFORCE_PARAM_PROTECTOR_ST import REINFORCE_PARAM_PROTECTOR_ST
from .REINFORCE_PARAM_WEAPON_ST import REINFORCE_PARAM_WEAPON_ST
from .SHADOW_BANK import SHADOW_BANK
from .SHOP_LINEUP_PARAM import SHOP_LINEUP_PARAM
from .SP_EFFECT_PARAM_ST import SP_EFFECT_PARAM_ST
from .SP_EFFECT_VFX_PARAM_ST import SP_EFFECT_VFX_PARAM_ST
from .TALK_PARAM_ST import TALK_PARAM_ST
from .THROW_INFO_BANK import THROW_INFO_BANK
from .TONE_CORRECT_BANK import TONE_CORRECT_BANK
from .TONE_MAP_BANK import TONE_MAP_BANK


if tp.TYPE_CHECKING:
    from soulstruct.base.params.utils import ParamFieldInfo


def get_param_info(param_type: str) -> dict:
    try:
        return globals()[param_type]
    except KeyError:
        raise KeyError(f"Could not find Param info for {param_type}.")


def get_param_info_field(param_type: str, field_name: str) -> ParamFieldInfo:
    param_info = get_param_info(param_type)
    field_hits = [field for field in param_info["fields"] if field.name == field_name]
    if not field_hits:
        raise ValueError(f"Could not find field {field_name} in param {param_type}.")
    return field_hits[0]
