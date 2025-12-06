
import re

def itemInRanges(item, ranges):
    for low, high in ranges:
        if item >= low and item <= high:
            return True
    return False

with open("inputs/5.txt") as file:
    ranges = []
    for line in file:
        if line.strip() == "":
            break
        match = re.match("(\d+)\-(\d+)", line)
        ranges.append((int(match.group(1)),int(match.group(2))))
    items = []
    for line in file:
        items.append(int(line.strip()))

    freshCount = 0
    for item in items:
        if itemInRanges(item, ranges):
            freshCount += 1

    print(freshCount)

    