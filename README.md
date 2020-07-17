# Basic RPG

**A CodeLouisville Project**
A simple command line role-playing game

### Installation and Running
- This project does not use any external libraries.
- Run `python3 play.py`

### Source Overview
This project consists of one class:
- `Character` sets values for name, attack, defense, weapon, armor, and hit points.
    - The `equip_weapon()` method sets the character object's weapon according to user prompts.
    - The `equip_armor()` method sets the character object's armor according to user prompts.

The game loop is in the `play.py` module.

The `battle.py` module contains the following functions:
- `battle()` is a loop that will run until the user chooses to exit or until the character or enemy reaches 0 hit points.
- `attack_command()` determines if an attack misses or hits and whether the damage reduces the target to 0 hit points.
- `attack_damage()` calculates and returns the damage value for each attack.

### Requirements
This project fulfills the following requirements:
- Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.
    - There are two loops: one in `battle.py` and the main loop in `play.py`. Exiting the loop in `play.py` will exit the program entirely.
- Create a class, then create at least one object of that class and populate it with data.
    - The `Character` class is used to create a character for the user. The object instance is created in the `characters.py` module.
- Read data from an external file, such as text, JSON, CSV, etc and use that data in your application.
    - Weapons and armor used by the `Character` class are read from the `weapons.csv` and `armor.csv` files, respectively.
- Create and call at least 3 functions, at least one of which must return a value that is used.
    - Multiple functions and methods can be found in all three `.py` modules.

**Additional Requirements**

- Your code have comments that document major sections of your code to make it easier to read.
- Your project code is uploaded to your GitHub account, in its own repository, with at least 5 commits.
- It must include a README file located at the top level directory of your project that includes:
    - A description of your project
    - What features you chose to included (so we know what to look for)
    - Any special instructions we might need to run your project
