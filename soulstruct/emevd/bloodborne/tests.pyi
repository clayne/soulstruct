from soulstruct.emevd.shared.tests import *
import soulstruct.game_types as gt

# Boolean constants.
HOST = ...
CLIENT = ...
SINGLEPLAYER = ...
MULTIPLAYER = ...

# Numeric comparison.
INSIGHT = ...

def IsAttackedWithDamageType(attacked_entity: gt.CharacterInt, attacking_character: gt.CharacterInt, damage_type): ...
def WearingArmorTypeInRange(armor_type, required_armor_range_first, required_armor_range_last): ...
def CharacterDrawGroupActive(character: gt.CharacterInt): ...
def CharacterDrawGroupInactive(character: gt.CharacterInt): ...
