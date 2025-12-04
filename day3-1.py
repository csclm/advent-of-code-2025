

def maxJoltage(bank):
    for firstDigit in range(9,-1,-1):
        try:
            firstDigitIndex = bank.index(firstDigit)
        except:
            continue
        if firstDigitIndex == len(bank) - 1:
            continue
        secondDigit = max(bank[firstDigitIndex+1:])
        return firstDigit * 10 + secondDigit
    raise Exception("Not possible?")

with open("inputs/3.txt") as file:
    totalMaxJoltage = 0
    for line in file:
        bank = [int(k) for k in line.strip()]
        totalMaxJoltage += maxJoltage(bank)
    print(totalMaxJoltage)











