import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "




def parse_input(input_string):
    """
    Returns 'input_string' as an interger between 1 and 6.

    Check if 'input_string' is an integer number between 1 and 6.
    If so, return an interger with the same value. Otherwise, tell the user to enter a valid number and quit the program.
    """
  

    try:
        input_int = int(input_string)
        if input_int < 1 or input_int > 6:
            print("Please enter a number from 1 to 6.")
            quit()
        elif 1 <= input_int <= 6:
            return input_int
        else:
            return input_int
    except ValueError:
        print('Please enter a valid number.')
        raise SystemExit





def roll_dice(num_dice):
    roll_results = []
    if num_dice is not None:
        for _ in range(num_dice):
            roll = random.randint(1, 6)
            roll_results.append(roll)





num_dice_input = input("How many dice would you like to roll?[1-6] ")
num_dice = parse_input(num_dice_input)
roll_results = roll_dice(num_dice)
