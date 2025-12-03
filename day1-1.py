
import re

with open("inputs/1.txt") as inputFile:
    timesLandedOnZero = 0
    currentDialNumber = 50
    for line in inputFile:
        match = re.match("([LR])(\d+)", line)
        if match.group(1) == "L":
            direction = -1
        else:
            direction = 1
        direction *= int(match.group(2))
        currentDialNumber += direction
        currentDialNumber %= 100
        if currentDialNumber == 0:
            timesLandedOnZero += 1
    print(timesLandedOnZero)