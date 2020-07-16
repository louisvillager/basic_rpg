import math
import random

import characters as char


goblin = char.Character('Goblin')
goblin.weapon = 'spiked club'
goblin.attack = 9
goblin.defense = 8

# For output messages only
if char.hero.weapon == '':
    char.hero.weapon = 'punch'

def battle():
    """The main loop of options in a battle."""

    goblin.hp = 30
    char.hero.hp = 50
    print('\nA goblin appears! What will you do?')

    # Round by Round
    combat = True
    while combat:
        options = '\n1. Attack\n'
        options += '2. Run\n\t'
        action = input(options)
        if action.lower() == 'attack' or action == '1':
            attack_command(char.hero, goblin)
            if goblin.hp <= 0:
                print('You have slain the goblin. Congratulations!')
                combat = False
            elif char.hero.hp <= 0:
                print('You were vanquished by a goblin. Thus ends a '
                'brief and inglorious adventuring career.')
                combat = False
        elif action.lower() == 'run' or action == '2':
            print('Well, they always said discretion is the better part '
            'of valor.'
            '\nBest to live and fight another day.')
            combat = False
        else:
            print('Please choose one of the available options.\n')

def attack_command(player_char, enemy):
    """Executes the steps of the attack command.
    For simplicity, the hero goes first, then the goblin.
    When either combatant reaches 0 HP, the combat ends.
    """

    if random.randint(1,5) == 1:
        print(f'{char.hero.name}\'s attack misses!')
    else:
        current_attack = attack_damage(char.hero.attack,
        goblin.defense)
        goblin.hp -= current_attack
        print(f'{char.hero.name} attacks with a {char.hero.weapon} '
        f'and deals {current_attack} damage.')
    if goblin.hp <= 0:
        return

    if random.randint(1,5) == 1:
        print('The goblin\'s attack misses!')
    else:
        current_attack = attack_damage(goblin.attack,
        char.hero.defense)
        char.hero.hp -= current_attack
        print(f'The goblin attacks with a {goblin.weapon} and deals '
        f'{current_attack} damage.')
        print(f'{char.hero.name} has {char.hero.hp} hit points left.')
    if char.hero.hp <= 0:
        return
    
def attack_damage(attack_val, defense_val):
    """Calculates damage for attack command.
    Uses attacking character's total attack vs. target's total defense,
    with slight random variance.
    """
    return math.ceil(attack_val * (random.randint(100,150)/100)
        - defense_val * (random.randint(20,30)/100))