# Creator: Aidan Scott
# Date: 9/23/24
# Description: This program implements an interactive scoring
#   system for a bowling game that displays a score sheet and
#   pin rack for the user. The project includes multiple
#   classes for different parts of the bowling score system.

# global constants
WELCOME_MESSAGE = "Bowling Score Sheet Simulation, \n\tPRESS ENTER TO CONTINUE"

# menu text
FIRST_MENU_OPTION = "Score Bowling Game"
EXIT_MENU_OPTION = "Exit Simulation"
PROMPT_MENU_CHOICE = "Please enter an option (1, 2, etc.) or enter X to exit: "
ERROR_INVALID_CHOICE = "Error: Invalid menu choice"
ERROR_INVALID_ENTRY = "Error: Invalid entry"
SHOT_SCORE_PROMPT_LINE_ONE_B1 = "Enter the pins knocked down for the first bowl"
SHOT_SCORE_PROMPT_LINE_ONE_B2 = "Enter the pins knocked down for the second bowl"
SHOT_SCORE_PROMPT_LINE_ONE_B3 = "Enter the pins knocked down for the third bowl"
SHOT_SCORE_PROMPT_LINE_TWO = "(use pin #'s and X for pin 10, do not include spaces): "

# menu values
VALUE_FIRST_MENU = "1"
VALUE_EXIT_MENU = "X"

# choice values align with the min and max numbers displayed in the menu
LOW_CHOICE_VALUE = 1
HIGH_CHOICE_VALUE = 1

# bowling values
PIN_LOWER_BOUND = 1
PIN_UPPER_BOUND = 10
STANDARD_FRAME_COUNT = 9
TENTH_FRAME_INDEX = 9
FIRST_SHOT_INDEX = 0
SECOND_SHOT_INDEX = 1
THIRD_SHOT_INDEX = 2
TOTAL_FRAME_COUNT = 10
DEFAULT_PIN_VALUE = True
PIN_DOWN_VALUE = False
EMPTY_FRAME = [0, 0]
PIN_DISPLAY_EDGE_LENGTH = 4
PIN_LABELS = [x for x in range(PIN_LOWER_BOUND, PIN_UPPER_BOUND + 1)]
PIN_RACK_LABELS = []
for x in range(PIN_LOWER_BOUND, PIN_UPPER_BOUND):
    PIN_RACK_LABELS.append(str(x))
PIN_RACK_LABELS.append("X")

from FrameClass import Frame, TenthFrame
from ScoreSheetClass import ScoreSheet
from PinRackClass import PinRack

def displayMenu():
    """
    Prints the contents of the menu.
    Takes no parameters and returns no values
    """
    print("1. " + FIRST_MENU_OPTION)
    print("X. " + EXIT_MENU_OPTION)

    return

def getPinsInput(pinRack, firstBowl, thirdBowl=False):
    """
    Function prompts for pins that were knocked down in a shot
        and updates the pin dictionary accordingly
    :param pinRack (PinRack): A PinRack object to keep track of which pins are downed
    :param firstBowl (booelan): True if collecting input for the first bowl
    :return: None
    """

    # create a list for user input string
    pinsDownList = []

    pinError = True

    while pinError:
        if firstBowl:
            pinsDownedInput = input(SHOT_SCORE_PROMPT_LINE_ONE_B1 +
                                    "\n\t" + SHOT_SCORE_PROMPT_LINE_TWO)
        elif (not firstBowl) and (not thirdBowl):
            pinsDownedInput = input(SHOT_SCORE_PROMPT_LINE_ONE_B2 +
                                    "\n\t" + SHOT_SCORE_PROMPT_LINE_TWO)
        elif thirdBowl:
            pinsDownedInput = input(SHOT_SCORE_PROMPT_LINE_ONE_B3 +
                                    "\n\t" + SHOT_SCORE_PROMPT_LINE_TWO)

        if pinsDownedInput == "":
            pinError = False

        elif pinsDownedInput in PIN_RACK_LABELS:
            # loop through the string and convert into a list (account for pin 10 as 'X')
            for char in pinsDownedInput:
                if char == 'X':
                    pinsDownList.append(int(PIN_UPPER_BOUND))
                elif char in PIN_LABELS:
                    try:
                        pinsDownList.append(int(char))
                    except ValueError:
                        print(ERROR_INVALID_ENTRY)
                    else:
                        for pin in pinsDownList:
                            if pin not in PIN_LABELS:
                                print(ERROR_INVALID_ENTRY)
                            else:
                                pinRack.setPin(pin, PIN_DOWN_VALUE)
                                pinError = False

        else:
            print(ERROR_INVALID_ENTRY)

    return

def simulateGame():
    """
    Function carries out a game of bowling with user
        prompts and displays of pins
    :return: None
    """
    # create score sheet for frames
    frameScores = ScoreSheet()

    pinRack = PinRack()

    # simulate the nine standard frames
    for frame in range(STANDARD_FRAME_COUNT):
        standardFrame(pinRack, frameScores, frame)

        frameScores.displayScoreSheet()
        print()

        pinRack.resetPins()

    # simulate unique tenth frame
    tenthFrame(pinRack, frameScores)

    frameScores.displayScoreSheet()

    return

def standardFrame(pinRack, frameScores, frame):
    """
    Function simulates a standard frame (frames 1-9) in a bowling game
    :param pinRack (PinRack): A pinRack object
    :param frameScores (ScoreSheet): The current ScoreSheet
        object for the game of bowling
    :param frame: The index value for the current frame
    :return:
    """
    # first shot
    firstBowl = True
    getPinsInput(pinRack, firstBowl)
    firstShotScore = pinRack.getPinScore()
    frameScores.getNthFrame(frame).setFirstBowl(firstShotScore)
    print(str(pinRack))

    if not frameScores.getNthFrame(frame).getStrike():
        firstBowl = False
        # second shot
        getPinsInput(pinRack, firstBowl)
        secondShotScore = pinRack.getPinScore()
        frameScores.getNthFrame(frame).setSecondBowl(secondShotScore - firstShotScore)
        print(str(pinRack))

    return

def tenthFrame(pinRack, frameScores):
    """
    Function simulates a standard frame (frames 1-9) in a bowling game
    :param pinRack (PinRack): A pinRack object
    :param frameScores (ScoreSheet): The current ScoreSheet
        object for the game of bowling
    :return:
    """
    firstBowl = True

    # first shot
    getPinsInput(pinRack, firstBowl)
    firstShotScore = pinRack.getPinScore()
    frameScores.getNthFrame(TENTH_FRAME_INDEX).setFirstBowl(firstShotScore)
    frameScores.displayScoreSheet()
    print(str(pinRack))
    print()

    # second shot
    firstBowl = False
    if frameScores.getNthFrame(TENTH_FRAME_INDEX).getFirstStrike():
        pinRack.resetPins()
        getPinsInput(pinRack, firstBowl)
        secondShotScore = pinRack.getPinScore()
        frameScores.getNthFrame(TENTH_FRAME_INDEX).setSecondBowl(secondShotScore)

    else:
        getPinsInput(pinRack, firstBowl)
        secondShotScore = pinRack.getPinScore()
        frameScores.getNthFrame(TENTH_FRAME_INDEX).setSecondBowl(secondShotScore - firstShotScore)

    frameScores.displayScoreSheet()
    print(str(pinRack))
    print()

    # third bowl
    thirdBowl = True
    if (frameScores.getNthFrame(TENTH_FRAME_INDEX).getSecondStrike()
            or frameScores.getNthFrame(TENTH_FRAME_INDEX).getSpare()):
        pinRack.resetPins()
        getPinsInput(pinRack, firstBowl, thirdBowl)
        thirdShotScore = pinRack.getPinScore()
        frameScores.getNthFrame(TENTH_FRAME_INDEX).setThirdBowl(thirdShotScore)

    frameScores.setCompleteGame(True)
    print(str(pinRack))

    return

def main():
    """
    Displays an interactive basic menu.
    """
    # print welcome message
    input(WELCOME_MESSAGE)

    exitMenu = False
    # menu exit loop
    while not exitMenu:

        validChoice = False
        # user input validation loop
        while not validChoice:
            # print the main menu
            displayMenu()

            # collect user input
            menuChoice = input(PROMPT_MENU_CHOICE)

            # exit the menu
            if menuChoice.upper() == VALUE_EXIT_MENU:
                exitMenu = True
                validChoice = True

            # check if the choice is within the bounds of the menu choice
            elif menuChoice.isnumeric():
                if LOW_CHOICE_VALUE <= int(menuChoice) <= HIGH_CHOICE_VALUE:
                    validChoice = True
                else:
                    print(ERROR_INVALID_CHOICE)
            else:
                print(ERROR_INVALID_CHOICE)

        # execute the code for each menu option
        if menuChoice == VALUE_FIRST_MENU:
            simulateGame()

    return

if __name__ == "__main__":
    main()
