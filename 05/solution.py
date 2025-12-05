def isItemInRange(item, ranges):
    for x, y in ranges:
        if item >= x and item <= y:
            return True
    return False


with open('input.txt') as file:
    data = file.read().split("\n\n")
    rangesRaw = data[0].split("\n")
    
    rangesData = []
    for r in rangesRaw:
        x, y = r.split('-')
        rangesData.append((int(x), int(y)))

    items = data[1].split("\n")
    ret = 0
    for item in items:
        if isItemInRange(int(item), rangesData):
            ret += 1
    print(ret)

