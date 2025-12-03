def getSmallestRepeatingSectionAboveX(x, numRepetitions):
    n = len(x)
    indexBeforeRepetition = n // numRepetitions

    if n % numRepetitions != 0:
        return "1" + "0" * indexBeforeRepetition

    left = x[:indexBeforeRepetition]
    repeated = left * numRepetitions

    if repeated >= x:
        return left
    else:
        return str(int(left) + 1)


def getLargestRepeatingSectionBelowX(x, numRepetitions):
    n = len(x)
    indexBeforeRepetition = n // numRepetitions

    if indexBeforeRepetition == 0:
        return "0"

    if n % numRepetitions != 0:
        return "9" * indexBeforeRepetition

    left = x[:indexBeforeRepetition]
    repeated = left * numRepetitions

    if repeated <= x:
        return left
    else:
        return str(int(left) - 1)


def sumInvalidNumbers(nums):
    ret = 0
    for x, y in nums:
        foundSet = set()
        for numRepetition in range(2, 10):
            a = int(getSmallestRepeatingSectionAboveX(x, numRepetition))
            b = int(getLargestRepeatingSectionBelowX(y, numRepetition))

            for i in range(a, b + 1):
                candidate = int(str(i) * numRepetition)
                if candidate not in foundSet:
                    ret += int(str(i) * numRepetition)
                    foundSet.add(candidate)
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
print(sumInvalidNumbers([["95", "115"]]) == 210)
print(sumInvalidNumbers([["998", "1012"]]) == 2009)
print(sumInvalidNumbers([["222220", "222224"]]) == 222222)
print(sumInvalidNumbers([["1188511880", "1188511890"]]) == 1188511885)
print(sumInvalidNumbers([["565653", "565659"]]) == 565656)
print(sumInvalidNumbers([["824824821", "824824827"]]) == 824824824)
print(sumInvalidNumbers([["2121212118", "2121212124"]]) == 2121212121)

