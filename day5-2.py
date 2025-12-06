
import re

def rangesOverlap(r1, r2):
    low1, high1 = r1
    low2, high2 = r2
    return numInRange(low1, r2) or numInRange(high1, r2) or (low1 < low2 and high1 > high2)

def numInRange(num, r):
    low, high = r
    return num >= low and num <= high

def mergeRanges(r1, r2):
    low1, high1 = r1
    low2, high2 = r2
    if numInRange(low1, r2):
        return (low2, max(high2, high1))
    elif numInRange(high1, r2):
        return (min(low2, low1), high2)
    elif low1 < low2 and high1 > high2:
        return (low1, high1)
    raise ValueError("can't merge non overlapping ranges")


with open("inputs/5.txt") as file:
    ranges = []
    for line in file:
        if line.strip() == "":
            break
        match = re.match("(\d+)\-(\d+)", line)
        ranges.append((int(match.group(1)),int(match.group(2))))
    
    unmergedLen = len(ranges)

    def findOverlappingRangesInList(ranges):
        for i1, r1 in enumerate(ranges):
            for i2, r2 in enumerate(ranges[i1+1:]):
                if rangesOverlap(r1, r2):
                    return (i1, i2+i1+1)
        return None

    while (overlap := findOverlappingRangesInList(ranges)) != None:
        i1, i2 = overlap
        ranges[i1] =  mergeRanges(ranges[i1], ranges[i2])
        ranges = ranges[:i2] + ranges[i2+1:]
    
    print(unmergedLen - len(ranges))
    totalIds = 0
    for low, high in ranges:
        totalIds += high-low+1
    print(totalIds)


    