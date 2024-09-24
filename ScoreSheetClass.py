# Creator: Aidan Scott
# Date: 9/14/24
# Description: This file contains a ScoreSheet
#   class that keeps track of the score for each
#   frame as well as the total and max possible score
import FrameClass

FRAME_UPPER_BOUND = 10
BORDER_LENGTH = 52
MARK_SCORE = 10
EIGHTH_FRAME_INDEX = 7
NINTH_FRAME_INDEX = 8
TENTH_FRAME_INDEX = 9
IN_PROGRESS_MESSAGE = "Game in progress..."

class ScoreSheet:
    def __init__(self):
        """
        Constructor
        """
        self.frameList = []
        self.totalScore = []

        # append nine standard frames
        for i in range(FRAME_UPPER_BOUND - 1):
            self.frameList.append(FrameClass.Frame())

        # append tenth frame
        self.frameList.append(FrameClass.TenthFrame())

        self.completeGame = False

    def getNthFrame(self, n):
        """
        Returns the frame at the index value of n in (0-9)
        :param n: the index value of the frame: Starting from 0-9
        """
        return self.frameList[n]

    def getTotalScore(self):
        """
        Gets the integer value of the total score
        :return (int): The total score represented as an integer
        """
        return self.totalScore

    def getCompleteGame(self):
        """
        Getter for whether the game has been fully bowled
        :return (boolean): True if the game is finished, False otherwise
        """
        return self.completeGame

    def setCompleteGame(self, other):
        """
        Setter for whether the game has been fully bowled
        :param other(boolean): Boolean value representing
            whether the game has been fully bowled
        :return: None
        """
        self.completeGame = other

        return

    def setTotalScore(self, other):
        """
        Sets the total score to a user-specified value
        :param other (int): An integer representing the
            total score for the game
        :return: None
        """
        self.totalScore = other

        return

    def displayScoreSheet(self):
        """
        Method displays the score sheet
        """
        self.printOuterBorderLine()  # top border
        self.printFrameLine()  # frame line
        self.printInnerBorderLine()  # inner border
        self.printScoreLine()  # score line
        self.printInnerBorderLine()  # interior border
        self.printTotalLine()  # total score line
        self.printOuterBorderLine()  # bottom border

        return

    def printOuterBorderLine(self):
        """
        Function prints the exterior top and bottom
        borders for the score sheet display
        """
        print("+", end="")
        for i in range(BORDER_LENGTH):
            print("=", end="")
        print("+")

    def printInnerBorderLine(self):
        """
        Function prints interior
        borders for the score sheet display
        """
        print("+", end="")
        for i in range(BORDER_LENGTH):
            print("-", end="")
        print("+")

    def printFrameLine(self):
        """
        Prints the line that lists the
        frames at the top of the score sheet
        """
        print("+ Frame:", end="")
        for i in range(1, FRAME_UPPER_BOUND + 1):
            print(f"| {i} ", end="")
        print(" |  +")

        return

    def printScoreLine(self):
        """
        Prints the line that list the scores of each frame
        """
        print("+ Score:", end="")
        for i in range(FRAME_UPPER_BOUND - 1):
            firstBowl = self.getNthFrame(i).getFirstBowl()
            secondBowl = self.getNthFrame(i).getSecondBowl()

            # format strike
            if firstBowl == 10:
                firstBowl = "X"
            elif firstBowl + secondBowl == 10:
                secondBowl = "/"

            # format 0 to -
            if firstBowl == 0:
                firstBowl = "-"
            if secondBowl == 0:
                secondBowl = "-"

            # format -1 to " "
            if firstBowl == -1:
                firstBowl = " "
            if secondBowl == -1:
                secondBowl = " "

            print(f"|{firstBowl} {secondBowl}", end="")

        tFirstBowl = self.getNthFrame(FRAME_UPPER_BOUND - 1).getFirstBowl()
        tSecondBowl = self.getNthFrame(FRAME_UPPER_BOUND - 1).getSecondBowl()
        tThirdBowl = self.getNthFrame(FRAME_UPPER_BOUND - 1).getThirdBowl()

        # format strikes
        if tFirstBowl == 10:
            tFirstBowl = "X"
        elif tFirstBowl + tSecondBowl == 10:
            tSecondBowl = "/"
        if tSecondBowl == 10:
            tSecondBowl = "X"
        elif tSecondBowl != "/" and tSecondBowl + tThirdBowl == 10:
            tThirdBowl = "/"
        if tThirdBowl == 10:
            tThirdBowl = "X"

        # format 0 to -
        if tFirstBowl == 0:
            tFirstBowl = "-"
        if tSecondBowl == 0:
            tSecondBowl = "-"
        if tThirdBowl == 0:
            tThirdBowl = "-"

        # format -1 to " "
        if tFirstBowl == -1:
            tFirstBowl = " "
        if tSecondBowl == -1:
            tSecondBowl = " "
        if tThirdBowl == -1:
            tThirdBowl = " "


        print(f"|{tFirstBowl} {tSecondBowl} {tThirdBowl}|  +")

        return

    def printTotalLine(self):
        # figure out how to print only at the end
        if self.getCompleteGame():
            print(f"+ Total Score: {self.calculateScore() : <38}+")
        else:
            print(f"+ Total Score: {IN_PROGRESS_MESSAGE:38}+")

    def calculateScore(self):
        """
        Function calculates a total score for
        a game given a complete frame list
        :return (int): The total score for the game
        """
        totalScore = 0

        # loop updates frame scores for spares and strikes
        for i in range(len(self.frameList)):

            # frames 1 - 7
            if i < EIGHTH_FRAME_INDEX:
                if self.frameList[i].getStrike():  # strike bowled
                    if self.frameList[i + 1].getStrike():  # strike in next frame
                        self.frameList[i].setFrameScore((MARK_SCORE
                            + self.frameList[i + 1].getFrameScore()
                            + self.frameList[i + 2].getFrameScore()))

                    else:  # next frame is open
                        self.frameList[i].setFrameScore((MARK_SCORE +
                            self.frameList[i + 1].getFrameScore()))

                elif self.frameList[i].getSpare():  # spare bowled
                    self.frameList[i].setFrameScore((MARK_SCORE +
                        self.frameList[i + 1].getFrameScore()))

            # eighth frame
            if i == EIGHTH_FRAME_INDEX:
                if self.frameList[i].getStrike():  # strike bowled
                    if self.frameList[i + 1].getStrike():
                        self.frameList[i].setFrameScore((MARK_SCORE +
                            self.frameList[i + 1].getFrameScore() +
                            self.frameList[i + 2].getFirstBowl()))
                    else:
                        self.frameList[i].setFrameScore((MARK_SCORE +
                            self.frameList[i + 1].getFrameScore()))

                elif self.frameList[i].getSpare():  # spare bowled
                    self.frameList[i].frameScore = MARK_SCORE + self.frameList[i + 1].getFirstBowl()

            # ninth frame
            if i == NINTH_FRAME_INDEX:
                if self.frameList[i].getStrike():  # strike bowled
                    self.frameList[i].setFrameScore((MARK_SCORE +
                        self.frameList[i + 1].getFirstBowl() +
                        self.frameList[i + 1].getSecondBowl()))
                elif self.frameList[i].getSpare():  # spare bowled
                    self.frameList[i].setFrameScore((MARK_SCORE +
                        self.frameList[i + 1].getFirstBowl()))

            # tenth frame
            if i == TENTH_FRAME_INDEX:
                if self.frameList[i].getFirstStrike():
                    self.frameList[i].setFrameScore((MARK_SCORE +
                        self.frameList[i].getSecondBowl() +
                        self.frameList[i].getThirdBowl()))

                elif self.frameList[i].getSpare():
                    self.frameList[i].setFrameScore((MARK_SCORE
                        + self.frameList[i].getThirdBowl()))

        # calculate final score
        for i in range(len(self.frameList)):
            totalScore += self.frameList[i].getFrameScore()

        self.setTotalScore(totalScore)  # update total score variable

        return totalScore

def main():
    scoreSheet = ScoreSheet()

    # load in example bowling game
    bowls = [10, -1, 9, 0, 5, 5, 10, -1, 0, 0, 2, 4, 10, -1, 9, 1, 10, -1]

    for i in range(0, len(bowls), 2):
        scoreSheet.getNthFrame(i // 2).setFirstBowl(bowls[i])
        scoreSheet.getNthFrame(i // 2).setSecondBowl(bowls[i + 1])

    scoreSheet.getNthFrame(FRAME_UPPER_BOUND - 1).setFirstBowl(10)
    scoreSheet.getNthFrame(FRAME_UPPER_BOUND - 1).setSecondBowl(9)
    scoreSheet.getNthFrame(FRAME_UPPER_BOUND - 1).setThirdBowl(1)

    scoreSheet.displayScoreSheet()
    # figure out the issue with not bowling a strike

if __name__ == "__main__":
    main()
