
def paperFromGrid(grid,row,col):
    if row < 0: return 0
    if col < 0: return 0
    if row > len(grid)-1: return 0
    if col > len(grid[0])-1: return 0
    return 1 if grid[row][col] == "@" else 0

def removeRolls(grid):
    outputGrid = [[col for col in row] for row in grid]
    rollsRemoved = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "@": continue
            rolls = 0
            rolls += paperFromGrid(grid,row-1,col-1)
            rolls += paperFromGrid(grid,row-1,col)
            rolls += paperFromGrid(grid,row-1,col+1)
            rolls += paperFromGrid(grid,row,col-1)
            rolls += paperFromGrid(grid,row,col+1)
            rolls += paperFromGrid(grid,row+1,col-1)
            rolls += paperFromGrid(grid,row+1,col)
            rolls += paperFromGrid(grid,row+1,col+1)
            if rolls < 4:
                outputGrid[row][col] = "."
                rollsRemoved += 1
    return (rollsRemoved, outputGrid)


with open("inputs/4.txt") as file:
    grid = [[char for char in line.strip()] for line in file]
    rollsRemoved = 0
    while True:
        removedThisTurn, grid = removeRolls(grid)
        if removedThisTurn == 0:
            break
        rollsRemoved += removedThisTurn
    print(rollsRemoved)
    

        

