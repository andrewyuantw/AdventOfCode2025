def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def buildNum(data, i):
    numBuilder = ''
    for j in range(len(data)):
        candidate = data[j][i]
        if is_int(candidate):
            numBuilder += candidate
    return int(numBuilder)

prevOperation = None
with open('real_input.txt') as file:
    data = file.read().split("\n")
    ret = 0
    currAccumulation = None
    prevOperation = None
    for i in range(len(data[0])):
        operation = data[-1][i]
        if prevOperation == None:
            prevOperation = operation

        isSeparatingColumn = True
        for j in range(len(data)):
            if data[j][i] != ' ':
                isSeparatingColumn = False
                break
        
        if not isSeparatingColumn:
            if prevOperation == '*':
                numToOperate = buildNum(data, i)
                if currAccumulation is None:
                    currAccumulation = numToOperate
                else:
                    currAccumulation *= numToOperate
            elif prevOperation == '+':
                numToOperate = buildNum(data, i)
                if currAccumulation is None:
                    currAccumulation = numToOperate
                else:
                    currAccumulation += numToOperate
        else:
            ret += currAccumulation
            currAccumulation = None
            prevOperation = None
    ret += currAccumulation
    print(ret)

