with open('real_input.txt') as file:
    data = file.read().split("\n")
    numSplits = 0
    indicesWithBeam = []
    for line in data:
        newIndicesWithBeam = []
        for i in range(len(line)):
            if line[i] == 'S':
                newIndicesWithBeam.append(i)
            elif line[i] == '^':
                if i in indicesWithBeam:
                    newIndicesWithBeam.append(i - 1)
                    newIndicesWithBeam.append(i + 1)
                    numSplits += 1
            else:
                if i in indicesWithBeam:
                    newIndicesWithBeam.append(i)
        indicesWithBeam = newIndicesWithBeam
    print(numSplits)
