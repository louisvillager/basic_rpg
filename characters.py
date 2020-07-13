import csv

class Character:
    def __init__(self, name):
        self.name = name
        self.base_attack = 3
        self.attack = 3
        self.base_defense = 1
        self.defense = 1
        self.weapon = ''
        self.armor = ''
        self.hp = 50

    def equip_weapon(self):
        # Equips weapon according to user prompts
        weap_type = input('What weapon type? (Slash, Pierce, Blunt?)  ')

        with open('weapons.csv', 'r') as f:
            weap_reader = csv.reader(f)

            for line in weap_reader:
                if weap_type == line[1]:
                    self.weapon = line[0]
                    self.attack = self.base_attack + int(line[2])
                    print(f'{self.name} equipped a {self.weapon}.')

    def equip_armor(self):
        # Equips armor according to user prompts
        arm_type = input('What armor type? (Mage, Light, or Heavy)  ')

        with open('armor.csv', 'r') as f:
            arm_reader = csv.reader(f)

            for line in arm_reader:
                if arm_type == line[1]:
                    self.armor = line[0]
                    self.defense = self.base_defense + int(line[2])
                    print(f'{self.name} equipped {self.armor} armor.')