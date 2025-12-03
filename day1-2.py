
import re

with open("inputs/1.txt") as inputFile:
    timesLandedOnZero = 0
    current = 50
    for line in inputFile:
        match = re.match("([LR])(\d+)", line)
        if match.group(1) == "L":
            direction = -1
        else:
            direction = 1
        magnitude = int(match.group(2))
        for _ in range(magnitude):
            current += direction
            current %= 100
            if current == 0:
                timesLandedOnZero += 1
    print(timesLandedOnZero)