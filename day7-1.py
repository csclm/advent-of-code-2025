with open ("inputs/7.txt") as file:
    grid = [[char for char in line] for line in file]

beams = set()
beams.add(grid[0].index("S"))

splits = 0
for row in grid:
    newBeams = set()
    for beam in beams:
        if row[beam] == "^":
            newBeams.add(beam-1)
            newBeams.add(beam+1)
            splits += 1
        else:
            newBeams.add(beam)
    beams = newBeams
            
print(splits)