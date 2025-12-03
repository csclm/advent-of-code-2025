
import re

def isIDValid(id):
    return id[:len(id)//2] * 2 != id

sumOfInvalidIDs = 0
with open("inputs/2.txt") as file:
    for line in file:
        for idRange in line.split(","):
            match = re.match(r"(\d+)\-(\d+)", idRange)
            low = int(match.group(1))
            high = int(match.group(2))
            for id in range(low, high+1):
                if not isIDValid(str(id)):
                    print(id)
                    sumOfInvalidIDs += id
        break # should only be one line

print(sumOfInvalidIDs)

