import csv


class Character:
    def __init__(self, name):
        """Initializes Character object and sets basic stats."""
        self.name = name
        self.base_attack = 3
        self.attack = 3
        self.base_defense = 1
        self.defense = 1
        self.weapon = ''
        self.armor = ''
        self.hp = 50

    def equip_weapon(self):
        """Equips weapon according to user prompts.
        Weapon stats are added to character base stats.
        Data is read from external CSV file.
        """
        weap_type = input('What weapon type? (Slash, Pierce, Blunt)  ')
        match = False

        with open('weapons.csv', 'r') as f:
            weap_reader = csv.reader(f)

            for line in weap_reader:
                if weap_type.lower() == line[1]:
                    self.weapon = line[0]
                    self.attack = self.base_attack + int(line[2])
                    print(f'{self.name} equipped a {self.weapon}.')
                    match = True

        if not match:
            print(f'Sorry, there is no {weap_type} weapon. Please try again.')

    def equip_armor(self):
        """Equips armor according to user prompts.
        Armor stats are added to character base stats.
        Data is read from external CSV file.
        """
        arm_type = input('What armor type? (Mage, Light, Heavy)  ')
        match = False

        with open('armor.csv', 'r') as f:
            arm_reader = csv.reader(f)

            for line in arm_reader:
                if arm_type.lower() == line[1]:
                    self.armor = line[0]
                    self.defense = self.base_defense + int(line[2])
                    print(f'{self.name} equipped {self.armor} armor.')
                    match = True

            if not match:
                print(f'Sorry, there is no {arm_type} armor. Please try again.')


# Initialize the player character at the start of the script
name_hero = input('Welcome to this basic RPG! Please name your '
    'character.  ')
hero = Character(name_hero)