import equipment

class Character:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = 50

    def equip(self):
        # Equips weapons and armor according to user prompts
        pass