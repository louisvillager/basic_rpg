class Weapon:
    def __init__(self, name, dmg_type, atk_val):
        self.name = name
        self.dmg_type = dmg_type  # bludgeoning, piercing, slashing
        self.atk_val = atk_val

class Armor:
    def __init__(self, name, arm_type, arm_val):
        self.name = name
        self.arm_type = arm_type  # light, mage, heavy
        self.arm_val = arm_val