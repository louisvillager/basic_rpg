import random

from characters import Character


def change_equip():
    # Allow player to change their equipment
    equip_option = input('\nWhich equipment would you like to change?'
        '\n1. Weapon'
        '\n2. Armor'
        '\n3. None\n\t')
    if equip_option.lower() == 'weapon' or equip_option == '1':
        hero.equip_weapon()
    elif equip_option.lower() == 'armor' or equip_option == '2':
        hero.equip_armor()
    else:
        pass

def battle():
    # Do battle with an enemy
    # Damage based on each character's weapon damage value and armor value
    pass


if __name__ == '__main__':
    # Main menu
    # EQUIPMENT
    # FIGHT
    # EXIT

    name_hero = input('Welcome to this basic RPG! Please name your character.  ')
    hero = Character(name_hero)
    print(f'\nAre you ready for adventure, {hero.name}? How will you proceed?')

    prompt =  '\n1. EQUIP - Change your character\'s equipment'
    prompt +=  '\n2. FIGHT - Do battle with an enemy'
    prompt +=  '\n3. EXIT - Exit the program\n\t'

    menu = True
    while menu == True:
        message = input(prompt)

        if message.upper() == 'EQUIP' or message == '1':
            change_equip()
        elif message.upper() == 'FIGHT' or message == '2':
            pass
        elif message.upper() == 'EXIT' or message == '3':
            print('Thank you for playing. Good bye!\n')
            menu = False
        else:
            print('Please choose one of the available options.')