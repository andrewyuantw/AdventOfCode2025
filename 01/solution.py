with open('input.txt') as file:
    data = file.read()
    lines = data.split("\n")
    position = 50
    ret = 0
    for line in lines:
        if line[0] == 'R':
            position += int(line[1:])
        else:
            position -= int(line[1:])
        if position % 100 == 0:
            ret += 1
    print(ret)