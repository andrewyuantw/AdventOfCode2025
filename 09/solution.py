with open('real_input.txt') as file:
    data = file.read().split("\n")
    ret = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x, y = [int(x) for x in data[i].split(",")]
            a, b = [int(x) for x in data[j].split(",")]
            ret = max(ret, (abs(x - a) + 1)  * (abs(y - b) + 1))
    print(ret)
