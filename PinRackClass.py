# Creator: Aidan Scott
# Date: 7/26/24
# Description: This file contains a class that represents a pin rack
#   in bowling. The main function gives a demonstration of the class.

PIN_LOWER_BOUND = 1
PIN_UPPER_BOUND = 10
PIN_DISPLAY_EDGE_LENGTH = 4
DEFAULT_PIN_VALUE = True
PIN_DOWN_VALUE = False

# creates a list from 1-10 that are integers used to refer to each pin
PIN_LABELS = [x for x in range(PIN_LOWER_BOUND, PIN_UPPER_BOUND + 1)]

ERROR_INVALID_ENTRY = "Error: Invalid entry"
SHOT_SCORE_PROMPT_LINE_ONE = "Enter the pins knocked down for the first bowl"
SHOT_SCORE_PROMPT_LINE_TWO = "(use pin #'s and X for pin 10, do not include spaces): "

class PinRack:
    def __init__(self):
        """
        Constructor:
        Creates a representation of a bowling pin rack using a dictionary
        """
        # represent pin rack as dictionary with True
        # if pin is standing and False otherwise
        self.pinDictionary = self.createPinDictionary()

    def createPinDictionary(self):
        """
        Creates a dictionary with pin numbers as keys
            and values are set to default pin values
        :return: A dictionary with pin numbers as keys,
            and the values are set to default pin values
        """
        # create bowling pins list
        pinList = [x for x in range(PIN_LOWER_BOUND, PIN_UPPER_BOUND + 1)]

        # create and populate dictionary of bowling pins
        pinDictionary = {}

        for pin in pinList:
            pinDictionary[pin] = DEFAULT_PIN_VALUE

        return pinDictionary

    def getPin(self, key):
        """
        Returns the boolean value stored for a user-given pin
        :param key: The label of the pin
        :return: Returns the boolean value stored for a specific pin
        """
        if key in self.pinDictionary:
            value = self.pinDictionary[key]
        else:
            value = None

        return value

    def setPin(self, key, value):
        """
        Sets the value of a pin to a user-specified value
        :param key: The label of the pin
        :param value: The value stored for the pin
        :return: None
        """
        if key in self.pinDictionary:
            self.pinDictionary[key] = value

        return

    def checkAllDowned(self):
        """
        Checks if all pins have been knocked down
        :return (bool): True if all pins are down, False otherwise
        """
        allPinsDowned = True

        for pin in self.pinDictionary:
            if self.pinDictionary[pin] == DEFAULT_PIN_VALUE:
                allPinsDowned = False

        return allPinsDowned

    def getPinScore(self):
        """
        Function takes the pin dictionary and counts amount of downed pins
        :return (int): score for the shot
        """
        score = 0

        for pin in self.pinDictionary:
            if self.pinDictionary[pin] == PIN_DOWN_VALUE:
                score += 1

        return score

    def resetPins(self):
        """
        Function sets all values in the pin
            dictionary back to their default state
        :return: None
        """
        for pin in self.pinDictionary:
            self.pinDictionary[pin] = DEFAULT_PIN_VALUE

        return

    def __str__(self):
        """
        Returns a string representation of the pin rack
        :return: a string representation of the pin rack
        """
        result = ""

        pinsList = PIN_LABELS.copy()

        # loop through list and replace values with X if not standing
        for pin in PIN_LABELS:
            key = pinsList[pin - 1]
            if not self.pinDictionary[key]:
                pinsList[pin - 1] = "X"

        pinsLeft = PIN_UPPER_BOUND

        for row in range(PIN_DISPLAY_EDGE_LENGTH, 0, -1):

            result += " "

            # assign spaces to the absolute value of rows minus length of triangle
            if row - 4 < 0:
                spaceCount = (row - 4) * -1
            else:
                spaceCount = row - 4

            # print the spaces for each row
            for space in range(spaceCount):
                result += " "

            # print the pins for each row
            for pin in range(pinsLeft - row, pinsLeft):
                result += str(pinsList[pin]) + " "
                pinsLeft -= 1

            # print empty line for the new row
            result += "\n"

        return result

def main():
    rack = PinRack()
    print(rack)

    # create a list for user input string
    pinsDownList = []

    pinError = True

    # get the pins from the user that were knocked down
    # NOTE: I did not put in the time to validate that the entry is correct
    while pinError:
        pinsDownedInput = input(SHOT_SCORE_PROMPT_LINE_ONE + "\n\t" + SHOT_SCORE_PROMPT_LINE_TWO)

        # loop through the string and convert into a list (account for pin 10 as 'X')
        for char in pinsDownedInput:
            if char == 'X':
                pinsDownList.append(int(PIN_UPPER_BOUND))
            else:
                pinsDownList.append(int(char))

        for pin in pinsDownList:
            if pin not in PIN_LABELS:
                print(ERROR_INVALID_ENTRY)
            else:
                rack.setPin(pin, PIN_DOWN_VALUE)
                pinError = False

    print(rack)

    print(f"The amount of pins knocked down is: {rack.getPinScore()}")
    print(f"All pins are knocked down = {rack.checkAllDowned()}")

    print("Resetting pin rack...\n")
    rack.resetPins()

    print(rack)
    return

if __name__ == "__main__":
    main()
