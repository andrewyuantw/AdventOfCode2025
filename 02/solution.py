def getSmallestRepeatingHalfAboveX(x):
    n = len(x)
    half = n // 2

    if n % 2 == 1:
        return "1" + "0" * half

    left = x[:half]
    repeated = left + left

    if repeated >= x:
        return left
    else:
        return str(int(left) + 1)


def getLargestRepeatingHalfBelowX(x: str) -> str:
    n = len(x)
    half = n // 2

    if n % 2 == 1:
        return "9" * half

    left = x[:half]
    repeated = left + left

    if repeated <= x:
        return left
    else:
        return str(int(left) - 1)


def sumInvalidNumbers(nums):
    ret = 0
    for x, y in nums:
        a = int(getSmallestRepeatingHalfAboveX(x))
        b = int(getLargestRepeatingHalfBelowX(y))

        for i in range(a, b + 1):
            ret += int(str(i) * 2)
    return ret


with open('input.txt') as file:
    data = file.read()
    ranges = data.split(",")
    nums = []
    for r in ranges:
        nums.append(r.split("-"))
    print(sumInvalidNumbers(nums))

# Test cases
print(sumInvalidNumbers([["11", "22"]]) == 33)
print(sumInvalidNumbers([["95", "115"]]) == 99)
print(sumInvalidNumbers([["998", "1012"]]) == 1010)
print(sumInvalidNumbers([["1188511880", "1188511890"]]) == 1188511885)
