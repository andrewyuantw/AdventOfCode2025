def getRotation(position):
    temp = position / 100
    if position < 0:
        temp -= 1
    return int(temp)

def process(nums):
    position = 50
    ret = 0
    for num in nums:
        oldRotation = getRotation(position)
        oldPosition = position
        startingAtZero = position % 100 == 0
        position += num
        newRotation = getRotation(position)
        if startingAtZero:
            ret += int(abs((position - oldPosition) / 100))
        else:
            if position % 100 == 0:
                ret += int(abs((position - oldPosition) / 100)) + 1
            elif oldRotation != newRotation:
                ret += abs(oldRotation - newRotation)
    return ret

with open('input.txt') as file:
    data = file.read()
    lines = data.split("\n")
    nums = []
    for line in lines:
        if line[0] == 'R':
            nums.append(int(line[1:]))
        else:
            nums.append(int(line[1:]) * -1)
    print(process(nums))

# Test cases
print(process([-50]) == 1)
print(process([1000]) == 10)
print(process([-50, 50]) == 1)
print(process([-50, 100]) == 2)
print(process([-50, -50]) == 1)
print(process([-50, -100]) == 2)
print(process([-50, 101]) == 2)
print(process([-50, 100, 200]) == 4)
print(process([-51, 100, 203]) == 5)
print(process([-50, -101, 200]) == 4)
print(process([-50, -101, 201]) == 5)
print(process([-50, 101, -201]) == 5)
print(process([149, -199]) == 3)