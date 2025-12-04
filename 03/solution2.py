DESIRED_FLIPS = 12

def sumMaxJoltage(joltages):
    ret = 0
    for digits in joltages:
        stack = []
        remaining = len(digits)

        for d in digits:
            while stack and stack[-1] < d and len(stack) - 1 + remaining >= DESIRED_FLIPS:
                stack.pop()
            stack.append(d)
            remaining -= 1

        ret += int("".join(stack[:DESIRED_FLIPS]))
    return ret


with open('input.txt') as file:
    data = file.read()
    joltages = data.split("\n")
    print(sumMaxJoltage(joltages))

# Test cases
print(sumMaxJoltage(["987654321111111"]) == 987654321111)
print(sumMaxJoltage(["811111111111119"]) == 811111111119)
print(sumMaxJoltage(["234234234234278"]) == 434234234278)
print(sumMaxJoltage(["818181911112111"]) == 888911112111)
print(sumMaxJoltage(["777688911112111"]) == 788911112111)
print(sumMaxJoltage(["119777777777879"]) == 977777777879)