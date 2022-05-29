from ftplib import all_errors
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
    return roll_results



def generate_dice_faces_diagram(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    width = len(dice_faces_rows[0])
    diagram_header = "RESULTS ".center(width, "=")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


def all_functions():
    num_dice_input = input("How many dice would you like to roll?[1-6] ")
    num_dice = parse_input(num_dice_input)
    roll_results = roll_dice(num_dice)
    dice_face_diagram = generate_dice_faces_diagram(roll_results)
    print(f"\n{dice_face_diagram}")
    print(f"\nYou rolled {num_dice} dice and got {sum(roll_results)}")
    return 
all_functions()
roll_again = input("Do you want to roll again?(y/n) ")
while roll_again == "y":
    if roll_again == "y":
        all_functions()
        roll_again = input("Do you want to roll again?(y/n) ")
        
 
    input("\nPress Enter to exit.")
    print("\nThanks for playing!")
 
        
