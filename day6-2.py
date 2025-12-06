from functools import reduce

def stripNewline(s):
    if s[-1] == "\n": return s[:-1]
    else: return s

with open("inputs/6.txt") as file:
    lines = [stripNewline(line) for line in file]
    transposed = [[line[col] for line in lines] for col in range(len(lines[0]))]
    problems = [[]]
    ops = []
    for col in transposed:
        print("".join(col))
        if "".join(col).strip() == "":
            problems.append([])
        elif col[-1] == "*" or col[-1] == "+":
            ops.append(col[-1])
            problems[-1].append(int("".join(col[:-1])))
        else:
            problems[-1].append(int("".join(col)))

    sumOfSolutions = 0
    for i in range(len(problems)):
        nums = problems[i]
        if ops[i] == "*": 
            solution = reduce(lambda x, y: x * y, nums, 1)
        else:
            solution = sum(nums)
        sumOfSolutions += solution

    print(sumOfSolutions)