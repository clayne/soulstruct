from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


EQUIP_MTRL_SET_PARAM_ST = {
    "param_type": "EQUIP_MTRL_SET_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "materialId01",
            "Material ID [1]",
            True,
            int,
            'Material item ID required to strengthen armor.',
        ),
        ParamFieldInfo(
            "materialId02",
            "Material ID [2]",
            True,
            int,
            'Material item ID required to strengthen armor.',
        ),
        ParamFieldInfo(
            "materialId03",
            "Material ID [3]",
            True,
            int,
            'Material item ID required to strengthen armor.',
        ),
        ParamFieldInfo(
            "materialId04",
            "Material ID [4]",
            True,
            int,
            'Material item ID required to strengthen armor.',
        ),
        ParamFieldInfo(
            "materialId05",
            "Material ID [5]",
            True,
            int,
            'Material item ID required to strengthen armor.',
        ),
        ParamFieldInfo(
            "materialId06",
            "Material ID [6]",
            True,
            int,
            'Material item ID required to strengthen armor.',
        ),
        ParamFieldInfo(
            "pad_id[8]",
            "Padding",
            False,
            pad_field(8),
            'Padding. For when the material item ID increases',
        ),
        ParamFieldInfo(
            "itemNum01",
            "Material Amount [1]",
            True,
            int,
            'The number of material items required to strengthen armor.',
        ),
        ParamFieldInfo(
            "itemNum02",
            "Material Amount [2]",
            True,
            int,
            'The number of material items required to strengthen armor.',
        ),
        ParamFieldInfo(
            "itemNum03",
            "Material Amount [3]",
            True,
            int,
            'The number of material items required to strengthen armor.',
        ),
        ParamFieldInfo(
            "itemNum04",
            "Material Amount [4]",
            True,
            int,
            'The number of material items required to strengthen armor.',
        ),
        ParamFieldInfo(
            "itemNum05",
            "Material Amount [5]",
            True,
            int,
            'The number of material items required to strengthen armor.',
        ),
        ParamFieldInfo(
            "itemNum06",
            "Material Amount [6]",
            True,
            int,
            'The number of material items required to strengthen armor.',
        ),
        ParamFieldInfo(
            "pad_num[2]",
            "Padding",
            False,
            pad_field(2),
            'Padding. For when the number of items increases',
        ),
        ParamFieldInfo(
            "materialCate01",
            "Material Category [1]",
            True,
            int,
            'This is a category of material items required for strengthening armor.',
        ),
        ParamFieldInfo(
            "materialCate02",
            "Material Category [2]",
            True,
            int,
            'This is a category of material items required for strengthening armor.',
        ),
        ParamFieldInfo(
            "materialCate03",
            "Material Category [3]",
            True,
            int,
            'This is a category of material items required for strengthening armor.',
        ),
        ParamFieldInfo(
            "materialCate04",
            "Material Category [4]",
            True,
            int,
            'This is a category of material items required for strengthening armor.',
        ),
        ParamFieldInfo(
            "materialCate05",
            "Material Category [5]",
            True,
            int,
            'This is a category of material items required for strengthening armor.',
        ),
        ParamFieldInfo(
            "materialCate06",
            "Material Category [6]",
            True,
            int,
            'This is a category of material items required for strengthening armor.',
        ),
        ParamFieldInfo(
            "pad_cate[2]",
            "Padding",
            False,
            pad_field(2),
            'Padding. For when the number of categories increases',
        ),
        ParamFieldInfo(
            "isDisableDispNum01:1",
            "Disable Display Number [1]",
            True,
            int,
            'Disable the number display (for enhanced shops)',
        ),
        ParamFieldInfo(
            "isDisableDispNum02:1",
            "Disable Display Number [2]",
            True,
            int,
            'Whether to disable the number display',
        ),
        ParamFieldInfo(
            "isDisableDispNum03:1",
            "Disable Display Number [3]",
            True,
            int,
            'Whether to disable the number display',
        ),
        ParamFieldInfo(
            "isDisableDispNum04:1",
            "Disable Display Number [4]",
            True,
            int,
            'Whether to disable the number display',
        ),
        ParamFieldInfo(
            "isDisableDispNum05:1",
            "Disable Display Number [5]",
            True,
            int,
            'Whether to disable the number display',
        ),
        ParamFieldInfo(
            "isDisableDispNum06:1",
            "Disable Display Number [6]",
            True,
            int,
            'Whether to disable the number display',
        ),
        ParamFieldInfo(
            "pad[3]",
            "Padding",
            False,
            pad_field(3),
            "It's padding.",
        ),
    ],
}
