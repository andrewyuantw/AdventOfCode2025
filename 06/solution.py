def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


with open('real_input.txt') as file:
    data = file.read().split("\n")
    processedData = []
    for row in data:
        numRow = []
        nums = row.split(" ")
        for num in nums:
            if num != "":
                if is_int(num):
                    numRow.append(int(num))
                else:
                    numRow.append(num)
        processedData.append(numRow)
    ret = 0
    for i in range(len(processedData[0])):
       
        operation = processedData[-1][i]
        if operation == "+":
            tempNum = 0
            for j in range(len(processedData) - 1):
                tempNum += processedData[j][i]
            ret += tempNum
        if operation == "*":
            tempNum = 1
            for j in range(len(processedData) - 1):
                tempNum *= processedData[j][i]
            ret += tempNum
    print(ret)

