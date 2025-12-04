def sumMaxJoltage(joltages):
    ret = 0
    for digits in joltages:
        nums = []
        for digit in digits:
            nums.append(int(digit))
        maxDigit = max(nums)
        if digits.index(str(maxDigit)) < len(digits) - 1:
            secondDigits = []
            for i in range(digits.index(str(maxDigit)) + 1, len(digits)):
                secondDigits.append(int(digits[i]))
            ret += 10 * maxDigit + max(secondDigits)
        else:
            nums.pop()
            firstDigit = max(nums)
            ret += 10 * firstDigit + maxDigit
    return ret


with open('input.txt') as file:
    data = file.read()
    joltages = data.split("\n")
    print(sumMaxJoltage(joltages))

