from functools import reduce

with open("inputs/6.txt") as file:
    lines = []
    for line in file:
        lines.append([element for element in line.split(" ") if len(element) > 0])
    ops = lines[-1]
    lines = lines[:-1]

    sumOfSolutions = 0
    for col in range(len(lines[0])):
        nums = [int(lines[row][col]) for row in range(len(lines))]
        if ops[col] == "*": 
            solution = reduce(lambda x, y: x * y, nums, 1)
        else:
            solution = sum(nums)
        sumOfSolutions += solution

    print(sumOfSolutions)
        


            

