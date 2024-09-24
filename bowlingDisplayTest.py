
def main():
    # create bowling pins tuple
    tempPins = [x for x in range(1, 11)]
    tPins = tuple(tempPins)
    
    # initialize a dictionary of pins
    pinsStanding = {}

    # each pin has a boolean associated for if it is standing or not
    for key in tPins:
        pinsStanding[key] = True
    
    # display pins
    print()
    displayPins(pinsStanding)


# function displays pins in traditional grid
def displayPins(pinsDictionary):
    # create list of pins
    pinsList = [x for x in range(1, 11)]

    # loop through list and replace values with X if not standing
    for pin in range(len(pinsList)):
        key = pinsList[pin]
        if not pinsDictionary[key]:
            pinsList[pin] = "X"

    pinsLeft = 10


    for row in range(4, 0, -1):

        print(" ", end="")

        # assign spaces to the absolute value of rows minus length of triangle
        if row - 4 < 0:
            spaceCount = (row - 4) * -1
        else:
            spaceCount = row - 4

        # print the spaces for each row
        for space in range(spaceCount):
            print(end=" ")

        # print the pins for each row
        for pin in range(pinsLeft - row, pinsLeft):
            print(pinsList[pin], end=" ")
            pinsLeft -= 1

        # print empty line for the new row
        print()

    return


main()
