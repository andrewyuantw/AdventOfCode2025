def combineRanges(ranges):
    combinedRangesData = []
    prevStart, prevEnd = None, None
    for x, y in ranges:
        if prevStart is None:
            prevStart, prevEnd = x, y
        else:
            if x > prevEnd:
                combinedRangesData.append((prevStart, prevEnd))
                prevStart, prevEnd = x, y
            else:
                prevEnd = max(y, prevEnd)
    
    combinedRangesData.append((prevStart, prevEnd))
    return combinedRangesData


with open('input.txt') as file:
    data = file.read().split("\n\n")
    rangesRaw = data[0].split("\n")
    
    rangesData = []
    for r in rangesRaw:
        x, y = r.split('-')
        rangesData.append((int(x), int(y)))
    
    rangesData = sorted(rangesData, key = lambda x: x[0])

    combinedRangesData = combineRanges(rangesData)
    ret = 0
    for x, y in combinedRangesData:
        ret += y - x + 1
    print(ret)


