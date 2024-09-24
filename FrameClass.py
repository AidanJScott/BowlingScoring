# Creator: Aidan Scott
# Date: 9/14/24
# Description: This file contains two classes to represent standard frames
#   and the tenth frame of bowling. The main function of this file gives a
#   demonstration of the classes

PIN_LOWER_BOUND = 0
PIN_UPPER_BOUND = 10

class Frame:
    def __init__(self, firstBowl=-1, secondBowl=-1):
        """
        Constructor:
        :param firstBowl: The pins knocked down in the first bowl
        :param secondBowl: The pins knocked down in the second bowl
        """
        self.bowled = False
        self.firstBowl = firstBowl
        self.secondBowl = secondBowl
        if firstBowl == -1:
            firstBowl = 0
        if secondBowl == -1:
            secondBowl = 0
        self.frameScore = firstBowl + secondBowl
        self.strike = False
        self.spare = False

        # update spare and strike values upon instantiation
        self.checkStrike()
        self.checkSpare()

    def getBowled(self):
        """
        Getter for whether the frame has begun to be bowled
        :return: True if the frame has begun to be bowled, False otherwise
        """
        return self.bowled

    def getFirstBowl(self):
        """
        Getter for the value of the first bowl
        :return: The pins knocked down in the first bowl
        """
        return self.firstBowl

    def getSecondBowl(self):
        """
        Getter for the value of the second bowl
        :return: The pins knocked down in the second bowl
        """
        return self.secondBowl

    def getFrameScore(self):
        """
        Getter for the amount of pins knocked down in the frame
        :return: The pins knocked down in the frame
        """
        return self.frameScore

    def getStrike(self):
        """
        Getter for if a strike was bowled in a frame
        :return: True if a strike was bowled, false otherwise
        """
        return self.strike

    def getSpare(self):
        """
        Getter for if a spare was bowled in a frame
        :return: True if a spare was bowled, false otherwise
        """
        return self.spare

    def setBowled(self, other):
        """
        Sets the value for whether the frame has begun to be bowled
        :param other (boolean): Boolean value representing whether
            the frame has begun to be bowled or not
        :return: None
        """
        self.bowled = other

        return

    def setFirstBowl(self, pinsDowned):
        """
        Set the value for the pins knocked down in the first bowl
            and updates the pins knocked down for the frame
        :param pinsDowned (int): An integer between 1-10 representing the
            amount of pins knocked down in the first frame
        :return: None
        """
        # update the total pins knocked down
        # and the amount of pins knocked down in the frame
        if str(pinsDowned).isdigit() and PIN_LOWER_BOUND <= pinsDowned <= PIN_UPPER_BOUND:
            self.firstBowl = pinsDowned
            self.checkFrameScore()

            # update strike variable if needed
            self.checkStrike()

        return

    def setSecondBowl(self, pinsDowned):
        """
        Set the value for the pins knocked down in the second bowl
            and updates the pins knocked down for the frame
        :param pinsDowned (int): An integer between 1-10 representing the
            amount of pins knocked down in the first frame
        :return: None
        """
        # update the total pins knocked down
        # and the amount of pins knocked down in the frame
        if str(pinsDowned).isdigit() and PIN_LOWER_BOUND <= pinsDowned <= PIN_UPPER_BOUND:
            self.secondBowl = pinsDowned
            self.checkFrameScore()

            # update spare variable if needed
            self.checkSpare()

        return

    def setFrameScore(self, score):
        """
        Set the value for the frameScore attribute
        :param score (int): An integer representing the
            total score calculated for the frame
        :return: None
        """
        self.frameScore = score

    def checkFrameScore(self):
        """
        Refresh the value of the frame's score by adding
            the first and second bowl together
        :return: None
        """
        if self.firstBowl == -1:
            firstBowl = 0
        else:
            firstBowl = self.firstBowl
        if self.secondBowl == -1:
            secondBowl = 0
        else:
            secondBowl = self.secondBowl
        self.frameScore = firstBowl + secondBowl
        return

    def checkStrike(self):
        """
        Checks if a strike was bowled in a frame,
            alters the strike variable if true
        :return: None
        """
        # check if ten pins were knocked down in the first frame
        if self.firstBowl == PIN_UPPER_BOUND:
            self.strike = True
        return

    def checkSpare(self):
        """
        Checks if a spare was bowled in a frame,
            alters spare variable if true
        :return: None
        """
        if self.firstBowl + self.secondBowl == PIN_UPPER_BOUND:
            self.spare = True

    def __str__(self):
        """
        Returns the string representation of a frame
        :return: The string representation of a frame
        """
        if self.strike:
            result = "[X]"
        elif self.spare:
            result = "[" + str(self.firstBowl) + ", /]"

        else:
            result = "[" + str(self.firstBowl) + ", " + str(self.secondBowl) + "]"

        return result

class TenthFrame(Frame):
    def __init__(self, firstBowl=-1, secondBowl=-1, thirdBowl=-1):
        """
        Constructor
        :param firstBowl: The score bowled for the first bowl
        :param secondBowl: The score bowled for the second bowl
        :param thirdBowl: The score bowled for the third bowl
        """
        Frame.__init__(self, firstBowl, secondBowl)

        self.thirdBowl = thirdBowl
        self.firstStrike = False
        self.secondStrike = False
        self.thirdStrike = False

        # check if a spare was bowled
        self.checkSpare()

        # check if strikes were bowled in any frames
        self.checkFirstStrike()
        self.checkSecondStrike()
        self.checkThirdStrike()

        return

    def getThirdBowl(self):
        """
        Getter for the value of the third bowl
        :return: The pins knocked down in the third bowl
        """
        return self.thirdBowl

    def getFirstStrike(self):
        """
        Getter for if the first bowl was a strike
        :return: True if a strike was bowled the first bowl,
            and False otherwise
        """
        return self.firstStrike

    def getSecondStrike(self):
        """
        Getter for if the second bowl was a strike
        :return: True if a strike was bowled the second bowl,
            and False otherwise
        """
        return self.secondStrike

    def getThirdStrike(self):
        """
        Getter for if the third bowl was a strike
        :return: True if a strike was bowled the third bowl.
            and False otherwise
        """
        return self.thirdStrike

    def setFirstBowl(self, pinsDowned):
        """
        Set the value for the pins knocked down in the first bowl
            and updates the pins knocked down for the frame
        :param pinsDowned (int): An integer between 1-10 representing the
            amount of pins knocked down in the first frame
        :return: None
        """
        # update the total pins knocked down
        # and the amount of pins knocked down in the frame
        if str(pinsDowned).isdigit() and PIN_LOWER_BOUND <= pinsDowned <= PIN_UPPER_BOUND:
            self.firstBowl = pinsDowned
            self.checkFrameScore()

            # update strike variable if needed
            self.checkFirstStrike()

        return

    def setSecondBowl(self, pinsDowned):
        """
        Set the value for the pins knocked down in the second bowl
            and updates the pins knocked down for the frame
        :param pinsDowned (int): An integer between 1-10 representing the
            amount of pins knocked down in the first frame
        :return: None
        """
        # update the total pins knocked down
        # and the amount of pins knocked down in the frame
        if str(pinsDowned).isdigit() and PIN_LOWER_BOUND <= pinsDowned <= PIN_UPPER_BOUND:
            self.secondBowl = pinsDowned
            self.checkFrameScore()

            # update spare and second strike variable if needed
            self.checkSpare()
            self.checkSecondStrike()

        return

    def setThirdBowl(self, pinsDowned):
        """
        Set the value for the pins knocked down in the first bowl
            and updates the pins knocked down for the frame
        :param pinsDowned (int): An integer between 1-10 representing the
            amount of pins knocked down in the first frame
        :return: None
        """
        # update the total pins knocked down
        # and the amount of pins knocked down in the frame
        if PIN_LOWER_BOUND <= pinsDowned <= PIN_UPPER_BOUND:
            self.thirdBowl = pinsDowned
            self.frameScore += pinsDowned

            # update strike variable if needed
            self.checkThirdStrike()

        return

    def checkFirstStrike(self):
        """
        Check if the first bowl was a strike,
            if so, set firstStrike variable to True
        :return: None
        """
        if self.firstBowl == PIN_UPPER_BOUND:
            self.firstStrike = True

        return

    def checkSecondStrike(self):
        """
        Check if the second bowl was a strike,
            if so, set secondStrike variable to True
        :return: None
        """
        if self.secondBowl == PIN_UPPER_BOUND:
            self.secondStrike = True

        return

    def checkThirdStrike(self):
        """
        Check if the third bowl was a strike,
            if so, set thirdStrike variable to True
        :return: None
        """
        if self.thirdBowl == PIN_UPPER_BOUND:
            self.thirdStrike = True
        return

    def __str__(self):
        """
        Returns the string representation of the tenth frame
        :return: The string representation of the tenth frame
        """
        # set the string values to be used in the result
        if self.firstStrike:
            firstBowl = "X"
        else:
            firstBowl = str(self.firstBowl)

        if self.secondStrike:
            secondBowl = "X"
        else:
            secondBowl = str(self.secondBowl)

        if self.thirdStrike:
            thirdBowl = "X"
        else:
            thirdBowl = str(self.thirdBowl)

        if self.spare:
            secondBowl = "/"

        result = "[" + firstBowl + ", " + secondBowl + ", " + thirdBowl + "]"

        return result

def main():
    """
    Main Function: Tests the Frame and TenthFrame classes
    """
    standardFrame = Frame(0, 0)
    print("Empty Frame: " + str(standardFrame))

    standardFrame.setFirstBowl(9)
    standardFrame.setSecondBowl(1)

    print("First Bowl: " + str(standardFrame.getFirstBowl()))
    print("Second Bowl: " + str(standardFrame.getSecondBowl()))
    print("Completed Frame" + str(standardFrame))
    print("Strike: " + str(standardFrame.getStrike()))
    print("Spare: " + str(standardFrame.getSpare()))

    tenthFrame = TenthFrame(0, 0, 0)
    print("Empty Tenth Frame: " + str(tenthFrame))

    tenthFrame.setFirstBowl(9)
    tenthFrame.setSecondBowl(1)
    tenthFrame.setThirdBowl(10)

    return

if __name__ == "__main__":
    main()