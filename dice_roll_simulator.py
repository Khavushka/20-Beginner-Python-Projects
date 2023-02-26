# import random
# define a function to roll the dice and return
# create a dictionary that will have the drawings of the dice 
# create a dictionary that will have the values of the dice 

import random

def roll_dice():

    dice_drawing = {
        1: {
            "┌───────┐",
            "|   ●   |",
            "|       |",    
            "└───────┘",
        },
        2: {
            "┌───────┐",
            "|  ●    |",
            "|    ●  |",
            "└───────┘",
        },
        3: {
            "┌───────┐",
            "|  ●    |",
            "|   ●   |",
            "|    ●  |",
            "└───────┘",
        },
        4: {
            "┌───────┐",
            "| ●   ● |",
            "| ●   ● |",
            "└───────┘",
        },
        5: {
            "┌───────┐",
            "| ●   ● |",
            "|   ●   |",
            "| ●   ● |",
            "└───────┘",
        },
        6: {
            "┌───────┐",
            "| ●   ● |",
            "| ●   ● |",
            "| ●   ● |",
            "└───────┘",
        },
    }

    roll = input("Roll the dice? (Yes/Now): ")
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))
        # print(dice_drawing[dice1])
        print("\n".join(dice_drawing[dice1]).encode('cp1252', errors='ignore'))
        print("\n".join(dice_drawing[dice2]).encode('cp1252', errors='ignore'))

        roll = input("Roll again? (Yes/Now): ")

roll_dice()
