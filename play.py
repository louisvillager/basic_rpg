import random
# import characters (or just Character class?)

def change_equip():
    # Allow player to change their equipment
    pass

def battle():
    # Do battle with an enemy
    # Damage based on each character's weapon damage value and armor value
    pass


if __name__ == '__main__':
    # Basic console menu
    # EQUIPMENT
    # FIGHT
    # EXIT
    # HELP

    prompt = 'Welcome to this basic RPG! Please choose an option:'
    prompt +=  '\n1. EQUIP - Change your character\'s equipment'
    prompt +=  '\n2. FIGHT - Do battle with an enemy'
    prompt +=  '\n3. EXIT - Exit the program\n\t'

    menu = True
    while menu == True:
        message = input(prompt)

        if message.upper() == 'EXIT' or message == '3':
            print('Thank you for playing. Good bye!')
            menu = False
        else:
            print('The loop works so far')