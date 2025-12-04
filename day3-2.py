

def maxJoltage(bank, batteries):
    if len(bank) < batteries:
        raise Exception("unsatisfiable")
    if batteries == 0:
        return 0
    for digit in range(9,-1,-1):
        try:
            digitIndex = bank.index(digit)
            return 10 ** (batteries-1) * digit + maxJoltage(bank[digitIndex+1:], batteries-1)
        except:
            continue

    raise Exception("Not possible")

with open("inputs/3.txt") as file:
    totalMaxJoltage = 0
    for line in file:
        bank = [int(k) for k in line.strip()]
        maxjolt= maxJoltage(bank, 12)
        print(maxjolt)
        totalMaxJoltage += maxjolt
    print(totalMaxJoltage)











