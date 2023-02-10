from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


HIT_EFFECT_SE_PARAM_ST = {
    "param_type": "HIT_EFFECT_SE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "Iron_Slash_S",
            "Iron - Slash: Small",
            True,
            int,
            'Iron: Slash: Small',
        ),
        ParamFieldInfo(
            "Iron_Slash_L",
            "Iron - Slash: Large",
            True,
            int,
            'Iron: Slash: Large',
        ),
        ParamFieldInfo(
            "Iron_Slash_LL",
            "Iron - Slash: Giant",
            True,
            int,
            'Iron: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Iron_Thrust_S",
            "Iron - Thrust: Small",
            True,
            int,
            'Iron: piercing: small',
        ),
        ParamFieldInfo(
            "Iron_Thrust_L",
            "Iron - Thrust: Large",
            True,
            int,
            'Made of iron: piercing: large',
        ),
        ParamFieldInfo(
            "Iron_Thrust_LL",
            "Iron - Thrust: Giant",
            True,
            int,
            'Iron: piercing: oversized',
        ),
        ParamFieldInfo(
            "Iron_Blow_S",
            "Iron - Strike: Small",
            True,
            int,
            'Iron: Batter: Small',
        ),
        ParamFieldInfo(
            "Iron_Blow_L",
            "Iron - Strike: Large",
            True,
            int,
            'Iron: Batter: Large',
        ),
        ParamFieldInfo(
            "Iron_Blow_LL",
            "Iron - Strike: Giant",
            True,
            int,
            'Iron: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Fire_Slash_S",
            "Fire - Slash: Small",
            True,
            int,
            'Flame: Slash: Small',
        ),
        ParamFieldInfo(
            "Fire_Slash_L",
            "Fire - Slash: Large",
            True,
            int,
            'Flame: Slash: Large',
        ),
        ParamFieldInfo(
            "Fire_Slash_LL",
            "Fire - Slash: Giant",
            True,
            int,
            'Flame: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Fire_Thrust_S",
            "Fire - Thrust: Small",
            True,
            int,
            'Flame: Piercing: Small',
        ),
        ParamFieldInfo(
            "Fire_Thrust_L",
            "Fire - Thrust: Large",
            True,
            int,
            'Flame: Piercing: Large',
        ),
        ParamFieldInfo(
            "Fire_Thrust_LL",
            "Fire - Thrust: Giant",
            True,
            int,
            'Flame: Piercing: Oversized',
        ),
        ParamFieldInfo(
            "Fire_Blow_S",
            "Fire - Strike: Small",
            True,
            int,
            'Flame: Batter: Small',
        ),
        ParamFieldInfo(
            "Fire_Blow_L",
            "Fire - Strike: Large",
            True,
            int,
            'Flame: Batter: Large',
        ),
        ParamFieldInfo(
            "Fire_Blow_LL",
            "Fire - Strike: Giant",
            True,
            int,
            'Flame: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Wood_Slash_S",
            "Wood - Slash: Small",
            True,
            int,
            'Wooden: Slash: Small',
        ),
        ParamFieldInfo(
            "Wood_Slash_L",
            "Wood - Slash: Large",
            True,
            int,
            'Wooden: Slash: Large',
        ),
        ParamFieldInfo(
            "Wood_Slash_LL",
            "Wood - Slash: Giant",
            True,
            int,
            'Wooden: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Wood_Thrust_S",
            "Wood - Thrust: Small",
            True,
            int,
            'Wooden: piercing: small',
        ),
        ParamFieldInfo(
            "Wood_Thrust_L",
            "Wood - Thrust: Large",
            True,
            int,
            'Wooden: piercing: large',
        ),
        ParamFieldInfo(
            "Wood_Thrust_LL",
            "Wood - Thrust: Giant",
            True,
            int,
            'Wooden: piercing: oversized',
        ),
        ParamFieldInfo(
            "Wood_Blow_S",
            "Wood - Strike: Small",
            True,
            int,
            'Wooden: Batter: Small',
        ),
        ParamFieldInfo(
            "Wood_Blow_L",
            "Wood - Strike: Large",
            True,
            int,
            'Wooden: Batter: Large',
        ),
        ParamFieldInfo(
            "Wood_Blow_LL",
            "Wood - Strike: Giant",
            True,
            int,
            'Wooden: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Body_Slash_S",
            "Flesh - Slash: Small",
            True,
            int,
            'Meat: Slash: Small',
        ),
        ParamFieldInfo(
            "Body_Slash_L",
            "Flesh - Slash: Large",
            True,
            int,
            'Meat: Slash: Large',
        ),
        ParamFieldInfo(
            "Body_Slash_LL",
            "Flesh - Slash: Giant",
            True,
            int,
            'Meat: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Body_Thrust_S",
            "Flesh - Thrust: Small",
            True,
            int,
            'Meat: Stab: Small',
        ),
        ParamFieldInfo(
            "Body_Thrust_L",
            "Flesh - Thrust: Large",
            True,
            int,
            'Meat: Stab: Large',
        ),
        ParamFieldInfo(
            "Body_Thrust_LL",
            "Flesh - Thrust: Giant",
            True,
            int,
            'Meat: Stab: Oversized',
        ),
        ParamFieldInfo(
            "Body_Blow_S",
            "Flesh - Strike: Small",
            True,
            int,
            'Meat: Batter: Small',
        ),
        ParamFieldInfo(
            "Body_Blow_L",
            "Flesh - Strike: Large",
            True,
            int,
            'Meat: Batter: Large',
        ),
        ParamFieldInfo(
            "Body_Blow_LL",
            "Flesh - Strike: Giant",
            True,
            int,
            'Meat: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Eclipse_Slash_S",
            "Corrosion - Slash: Small",
            True,
            int,
            'Corrosion: Slash: Small',
        ),
        ParamFieldInfo(
            "Eclipse_Slash_L",
            "Corrosion - Slash: Large",
            True,
            int,
            'Eating: Slashing: Large',
        ),
        ParamFieldInfo(
            "Eclipse_Slash_LL",
            "Corrosion - Slash: Giant",
            True,
            int,
            'Eating: Slashing: Oversized',
        ),
        ParamFieldInfo(
            "Eclipse_Thrust_S",
            "Corrosion - Thrust: Small",
            True,
            int,
            'Corrosion: piercing: small',
        ),
        ParamFieldInfo(
            "Eclipse_Thrust_L",
            "Corrosion - Thrust: Large",
            True,
            int,
            'Corrosion: Piercing: Large',
        ),
        ParamFieldInfo(
            "Eclipse_Thrust_LL",
            "Corrosion - Thrust: Giant",
            True,
            int,
            'Corrosion: piercing: oversized',
        ),
        ParamFieldInfo(
            "Eclipse_Blow_S",
            "Corrosion - Strike: Small",
            True,
            int,
            'Corrosion: Batter: Small',
        ),
        ParamFieldInfo(
            "Eclipse_Blow_L",
            "Corrosion - Strike: Large",
            True,
            int,
            'Corrosion: Batter: Large',
        ),
        ParamFieldInfo(
            "Eclipse_Blow_LL",
            "Corrosion - Strike: Giant",
            True,
            int,
            'Corrosion: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Energy_Slash_S",
            "Energy - Slash: Small",
            True,
            int,
            'Energy: Slash: Small',
        ),
        ParamFieldInfo(
            "Energy_Slash_L",
            "Energy - Slash: Large",
            True,
            int,
            'Energy: Slash: Large',
        ),
        ParamFieldInfo(
            "Energy_Slash_LL",
            "Energy - Slash: Giant",
            True,
            int,
            'Energy: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Energy_Thrust_S",
            "Energy - Thrust: Small",
            True,
            int,
            'Energy: Puncture: Small',
        ),
        ParamFieldInfo(
            "Energy_Thrust_L",
            "Energy - Thrust: Large",
            True,
            int,
            'Energy: Puncture: Large',
        ),
        ParamFieldInfo(
            "Energy_Thrust_LL",
            "Energy - Thrust: Giant",
            True,
            int,
            'Energy: Puncture: Oversized',
        ),
        ParamFieldInfo(
            "Energy_Blow_S",
            "Energy - Strike: Small",
            True,
            int,
            'Energy: Batter: Small',
        ),
        ParamFieldInfo(
            "Energy_Blow_L",
            "Energy - Strike: Large",
            True,
            int,
            'Energy: Batter: Large',
        ),
        ParamFieldInfo(
            "Energy_Blow_LL",
            "Energy - Strike: Giant",
            True,
            int,
            'Energy: Batter: Oversized',
        ),
        ParamFieldInfo(
            "None_Slash_S",
            "None - Slash: Small",
            True,
            int,
            'None: Slash: Small',
        ),
        ParamFieldInfo(
            "None_Slash_L",
            "None - Slash: Large",
            True,
            int,
            'None: Slash: Large',
        ),
        ParamFieldInfo(
            "None_Slash_LL",
            "None - Slash: Giant",
            True,
            int,
            'None: Slash: Oversized',
        ),
        ParamFieldInfo(
            "None_Thrust_S",
            "None - Thrust: Small",
            True,
            int,
            'None: Piercing: Small',
        ),
        ParamFieldInfo(
            "None_Thrust_L",
            "None - Thrust: Large",
            True,
            int,
            'None: Piercing: Large',
        ),
        ParamFieldInfo(
            "None_Thrust_LL",
            "None - Thrust: Giant",
            True,
            int,
            'None: Piercing: Oversized',
        ),
        ParamFieldInfo(
            "None_Blow_S",
            "None - Strike: Small",
            True,
            int,
            'None: Batter: Small',
        ),
        ParamFieldInfo(
            "None_Blow_L",
            "None - Strike: Large",
            True,
            int,
            'None: Batter: Large',
        ),
        ParamFieldInfo(
            "None_Blow_LL",
            "None - Strike: Giant",
            True,
            int,
            'None: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Dmy1_Slash_S",
            "Dummy 1 - Slash: Small",
            True,
            int,
            'Dmy1: Slash: Small',
        ),
        ParamFieldInfo(
            "Dmy1_Slash_L",
            "Dummy 1 - Slash: Large",
            True,
            int,
            'Dmy1: Slash: Large',
        ),
        ParamFieldInfo(
            "Dmy1_Slash_LL",
            "Dummy 1 - Slash: Giant",
            True,
            int,
            'Dmy1: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Dmy1_Thrust_S",
            "Dummy 1 - Thrust: Small",
            True,
            int,
            'Dmy1: Stab: Small',
        ),
        ParamFieldInfo(
            "Dmy1_Thrust_L",
            "Dummy 1 - Thrust: Large",
            True,
            int,
            'Dmy1: Stab: Large',
        ),
        ParamFieldInfo(
            "Dmy1_Thrust_LL",
            "Dummy 1 - Thrust: Giant",
            True,
            int,
            'Dmy1: Stab: Oversized',
        ),
        ParamFieldInfo(
            "Dmy1_Blow_S",
            "Dummy 1 - Strike: Small",
            True,
            int,
            'Dmy1: Batter: Small',
        ),
        ParamFieldInfo(
            "Dmy1_Blow_L",
            "Dummy 1 - Strike: Large",
            True,
            int,
            'Dmy1: Batter: Large',
        ),
        ParamFieldInfo(
            "Dmy1_Blow_LL",
            "Dummy 1 - Strike: Giant",
            True,
            int,
            'Dmy1: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Dmy2_Slash_S",
            "Dummy 2 - Slash: Small",
            True,
            int,
            'Dmy2: Slash: Small',
        ),
        ParamFieldInfo(
            "Dmy2_Slash_L",
            "Dummy 2 - Slash: Large",
            True,
            int,
            'Dmy2: Slash: Large',
        ),
        ParamFieldInfo(
            "Dmy2_Slash_LL",
            "Dummy 2 - Slash: Giant",
            True,
            int,
            'Dmy2: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Dmy2_Thrust_S",
            "Dummy 2 - Thrust: Small",
            True,
            int,
            'Dmy2: Piercing: Small',
        ),
        ParamFieldInfo(
            "Dmy2_Thrust_L",
            "Dummy 2 - Thrust: Large",
            True,
            int,
            'Dmy2: Piercing: Large',
        ),
        ParamFieldInfo(
            "Dmy2_Thrust_LL",
            "Dummy 2 - Thrust: Giant",
            True,
            int,
            'Dmy2: Piercing: Oversized',
        ),
        ParamFieldInfo(
            "Dmy2_Blow_S",
            "Dummy 2 - Strike: Small",
            True,
            int,
            'Dmy2: Batter: Small',
        ),
        ParamFieldInfo(
            "Dmy2_Blow_L",
            "Dummy 2 - Strike: Large",
            True,
            int,
            'Dmy2: Batter: Large',
        ),
        ParamFieldInfo(
            "Dmy2_Blow_LL",
            "Dummy 2 - Strike: Giant",
            True,
            int,
            'Dmy2: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Dmy3_Slash_S",
            "Dummy 3 - Slash: Small",
            True,
            int,
            'Dmy3: Slash: Small',
        ),
        ParamFieldInfo(
            "Dmy3_Slash_L",
            "Dummy 3 - Slash: Large",
            True,
            int,
            'Dmy3: Slash: Large',
        ),
        ParamFieldInfo(
            "Dmy3_Slash_LL",
            "Dummy 3 - Slash: Giant",
            True,
            int,
            'Dmy3: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Dmy3_Thrust_S",
            "Dummy 3 - Thrust: Small",
            True,
            int,
            'Dmy3: Piercing: Small',
        ),
        ParamFieldInfo(
            "Dmy3_Thrust_L",
            "Dummy 3 - Thrust: Large",
            True,
            int,
            'Dmy3: Piercing: Large',
        ),
        ParamFieldInfo(
            "Dmy3_Thrust_LL",
            "Dummy 3 - Thrust: Giant",
            True,
            int,
            'Dmy3: Piercing: Oversized',
        ),
        ParamFieldInfo(
            "Dmy3_Blow_S",
            "Dummy 3 - Strike: Small",
            True,
            int,
            'Dmy3: Batter: Small',
        ),
        ParamFieldInfo(
            "Dmy3_Blow_L",
            "Dummy 3 - Strike: Large",
            True,
            int,
            'Dmy3: Batter: Large',
        ),
        ParamFieldInfo(
            "Dmy3_Blow_LL",
            "Dummy 3 - Strike: Giant",
            True,
            int,
            'Dmy3: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Maggot_Slash_S",
            "Maggot - Slash: Small",
            True,
            int,
            'Uji: Slash: Small',
        ),
        ParamFieldInfo(
            "Maggot_Slash_L",
            "Maggot - Slash: Large",
            True,
            int,
            'Uji: Slash: Large',
        ),
        ParamFieldInfo(
            "Maggot_Slash_LL",
            "Maggot - Slash: Giant",
            True,
            int,
            'Uji: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Maggot_Thrust_S",
            "Maggot - Thrust: Small",
            True,
            int,
            'Uji: Stab: Small',
        ),
        ParamFieldInfo(
            "Maggot_Thrust_L",
            "Maggot - Thrust: Large",
            True,
            int,
            'Uji: Stab: Large',
        ),
        ParamFieldInfo(
            "Maggot_Thrust_LL",
            "Maggot - Thrust: Giant",
            True,
            int,
            'Uji: Stab: Oversized',
        ),
        ParamFieldInfo(
            "Maggot_Blow_S",
            "Maggot - Strike: Small",
            True,
            int,
            'Uji: Batter: Small',
        ),
        ParamFieldInfo(
            "Maggot_Blow_L",
            "Maggot - Strike: Large",
            True,
            int,
            'Uji: Batter: Large',
        ),
        ParamFieldInfo(
            "Maggot_Blow_LL",
            "Maggot - Strike: Giant",
            True,
            int,
            'Uji: Batter: Oversized',
        ),
        ParamFieldInfo(
            "Wax_Slash_S",
            "Wax - Slash: Small",
            True,
            int,
            'Wax: Slash: Small',
        ),
        ParamFieldInfo(
            "Wax_Slash_L",
            "Wax - Slash: Large",
            True,
            int,
            'Wax: Slash: Large',
        ),
        ParamFieldInfo(
            "Wax_Slash_LL",
            "Wax - Slash: Giant",
            True,
            int,
            'Wax: Slash: Oversized',
        ),
        ParamFieldInfo(
            "Wax_Thrust_S",
            "Wax - Thrust: Small",
            True,
            int,
            'Wax: piercing: small',
        ),
        ParamFieldInfo(
            "Wax_Thrust_L",
            "Wax - Thrust: Large",
            True,
            int,
            'Wax: piercing: large',
        ),
        ParamFieldInfo(
            "Wax_Thrust_LL",
            "Wax - Thrust: Giant",
            True,
            int,
            'Wax: piercing: oversized',
        ),
        ParamFieldInfo(
            "Wax_Blow_S",
            "Wax - Strike: Small",
            True,
            int,
            'Wax: Batter: Small',
        ),
        ParamFieldInfo(
            "Wax_Blow_L",
            "Wax - Strike: Large",
            True,
            int,
            'Wax: Batter: Large',
        ),
        ParamFieldInfo(
            "Wax_Blow_LL",
            "Wax - Strike: Giant",
            True,
            int,
            'Wax: Batter: Oversized',
        ),
        ParamFieldInfo(
            "FireFlame_Slash_S",
            "Burning - Slash: Small",
            True,
            int,
            'Burning: Slashing: Small',
        ),
        ParamFieldInfo(
            "FireFlame_Slash_L",
            "Burning - Slash: Large",
            True,
            int,
            'Burning: Slashing: Large',
        ),
        ParamFieldInfo(
            "FireFlame_Slash_LL",
            "Burning - Slash: Giant",
            True,
            int,
            'Burning: Slashing: Oversized',
        ),
        ParamFieldInfo(
            "FireFlame_Thrust_S",
            "Burning - Thrust: Small",
            True,
            int,
            'Burning: Piercing: Small',
        ),
        ParamFieldInfo(
            "FireFlame_Thrust_L",
            "Burning - Thrust: Large",
            True,
            int,
            'Burning: Piercing: Large',
        ),
        ParamFieldInfo(
            "FireFlame_Thrust_LL",
            "Burning - Thrust: Giant",
            True,
            int,
            'Burning: Piercing: Oversized',
        ),
        ParamFieldInfo(
            "FireFlame_Blow_S",
            "Burning - Strike: Small",
            True,
            int,
            'On fire: Batter: Small',
        ),
        ParamFieldInfo(
            "FireFlame_Blow_L",
            "Burning - Strike: Large",
            True,
            int,
            'On fire: Batter: Large',
        ),
        ParamFieldInfo(
            "FireFlame_Blow_LL",
            "Burning - Strike: Giant",
            True,
            int,
            'On fire: Batter: Oversized',
        ),
        ParamFieldInfo(
            "EclipseGas_Slash_S",
            "Corrosion Gas - Slash: Small",
            True,
            int,
            'Corrosion: Gas: Slash: Small',
        ),
        ParamFieldInfo(
            "EclipseGas_Slash_L",
            "Corrosion Gas - Slash: Large",
            True,
            int,
            'Corrosion: Gas: Slash: Large',
        ),
        ParamFieldInfo(
            "EclipseGas_Slash_LL",
            "Corrosion Gas - Slash: Giant",
            True,
            int,
            'Corrosion: Gas: Slash: Oversized',
        ),
        ParamFieldInfo(
            "EclipseGas_Thrust_S",
            "Corrosion Gas - Thrust: Small",
            True,
            int,
            'Corrosion: Gas: Piercing: Small',
        ),
        ParamFieldInfo(
            "EclipseGas_Thrust_L",
            "Corrosion Gas - Thrust: Large",
            True,
            int,
            'Corrosion: Gas: Piercing: Large',
        ),
        ParamFieldInfo(
            "EclipseGas_Thrust_LL",
            "Corrosion Gas - Thrust: Giant",
            True,
            int,
            'Corrosion: Gas: Piercing: Oversized',
        ),
        ParamFieldInfo(
            "EclipseGas_Blow_S",
            "Corrosion Gas - Strike: Small",
            True,
            int,
            'Corrosion: Gas: Batter: Small',
        ),
        ParamFieldInfo(
            "EclipseGas_Blow_L",
            "Corrosion Gas - Strike: Large",
            True,
            int,
            'Corrosion: Gas: Batter: Large',
        ),
        ParamFieldInfo(
            "EclipseGas_Blow_LL",
            "Corrosion Gas - Strike: Giant",
            True,
            int,
            'Corrosion: Gas: Batter: Oversized',
        ),
        ParamFieldInfo(
            "EnergyStrong_Slash_S",
            "Strong Energy - Slash: Small",
            True,
            int,
            'Energy (strong): Slash: Small',
        ),
        ParamFieldInfo(
            "EnergyStrong_Slash_L",
            "Strong Energy - Slash: Large",
            True,
            int,
            'Energy (strong): Slash: Large',
        ),
        ParamFieldInfo(
            "EnergyStrong_Slash_LL",
            "Strong Energy - Slash: Giant",
            True,
            int,
            'Energy (strong): Slash: Oversized',
        ),
        ParamFieldInfo(
            "EnergyStrong_Thrust_S",
            "Strong Energy - Thrust: Small",
            True,
            int,
            'Energy (strong): piercing: small',
        ),
        ParamFieldInfo(
            "EnergyStrong_Thrust_L",
            "Strong Energy - Thrust: Large",
            True,
            int,
            'Energy (strong): piercing: large',
        ),
        ParamFieldInfo(
            "EnergyStrong_Thrust_LL",
            "Strong Energy - Thrust: Giant",
            True,
            int,
            'Energy (strong): piercing: oversized',
        ),
        ParamFieldInfo(
            "EnergyStrong_Blow_S",
            "Strong Energy - Strike: Small",
            True,
            int,
            'Energy (strong): Batter: Small',
        ),
        ParamFieldInfo(
            "EnergyStrong_Blow_L",
            "Strong Energy - Strike: Large",
            True,
            int,
            'Energy (strong): Batter: Large',
        ),
        ParamFieldInfo(
            "EnergyStrong_Blow_LL",
            "Strong Energy - Strike: Giant",
            True,
            int,
            'Energy (strong): Batter: Oversized',
        ),
        ParamFieldInfo(
            "reserve[100]",
            "Reserved area",
            False,
            pad_field(100),
            'Reserved area',
        ),
    ],
}
