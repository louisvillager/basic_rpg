import random

import battle
import characters


def change_equip():
    """Allows player to change their equipment"""
    equip_option = input('\nWhich equipment would you like to change?'
        '\n1. Weapon'
        '\n2. Armor'
        '\n3. None\n\t')
    if equip_option.lower() == 'weapon' or equip_option == '1':
        characters.hero.equip_weapon()
    elif equip_option.lower() == 'armor' or equip_option == '2':
        characters.hero.equip_armor()
    else:
        pass


if __name__ == '__main__':
    """Main loop.
    User has the option to change equipment, fight a monster, or exit
    the program.
    """

    print(f'\nAre you ready for adventure, {characters.hero.name}? '
        'How will you proceed?')

    prompt =  '\n1. EQUIP - Change your character\'s equipment'
    prompt +=  '\n2. FIGHT - Do battle with an enemy'
    prompt +=  '\n3. EXIT - Exit the program\n\t'

    # Main Menu
    # Will loop indefinitely until user chooses to EXIT
    menu = True
    while menu == True:
        message = input(prompt)

        if message.upper() == 'EQUIP' or message == '1':
            change_equip()
        elif message.upper() == 'FIGHT' or message == '2':
            battle.battle()
        elif message.upper() == 'EXIT' or message == '3':
            print('Thank you for playing. Good bye!\n')
            menu = False
        else:
            print('Please choose one of the available options.')