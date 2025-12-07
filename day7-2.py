with open ("inputs/7.txt") as file:
    grid = [[char for char in line] for line in file]

beams = dict()
beams[grid[0].index("S")] = 1
for row in grid:
    newBeams = dict()
    for beam in beams:
        if row[beam] == "^":
            if beam-1 not in newBeams:
                newBeams[beam-1] = 0
            if beam+1 not in newBeams:
                newBeams[beam+1] = 0
            newBeams[beam-1] += beams[beam]
            newBeams[beam+1] += beams[beam]
        else:
            if beam not in newBeams:
                newBeams[beam] = 0
            newBeams[beam]+=beams[beam]

    for i, char in enumerate(row):
        if i in newBeams:
            print(newBeams[i], end="")
        else:
            print(row[i], end = "")
        print(" ", end = "")
    print()

    beams = newBeams


print(sum((ways for ways in beams.values()))) 