from collections import defaultdict
with open('real_input.txt') as file:
    data = file.read().split("\n")
    numSplits = 0
    indicesWithBeam = {}
    for line in data:
        newIndicesWithBeam = defaultdict(int)
        for i in range(len(line)):
            if line[i] == 'S':
                newIndicesWithBeam[i] = 1
            elif line[i] == '^':
                if i in indicesWithBeam:
                    newIndicesWithBeam[i - 1] += indicesWithBeam[i]
                    newIndicesWithBeam[i + 1] += indicesWithBeam[i]
            else:
                if i in indicesWithBeam:
                    newIndicesWithBeam[i] += indicesWithBeam[i]
        indicesWithBeam = newIndicesWithBeam
    ret = 0
    for key in indicesWithBeam:
        ret += indicesWithBeam[key]
    print(ret)
