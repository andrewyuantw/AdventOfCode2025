import heapq
from unionfind import unionfind

min_heap = []

NUM_CONNECTIONS_TO_MAKE = 1000

uniqueIdsMap = {}
uniqueIdCounter = 1

with open('real_input.txt') as file:
    data = file.read().split("\n")
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x, y , z = [int(a) for a in data[i].split(",")]
            x2, y2, z2 = [int(a) for a in data[j].split(",")]

            distance = ((x - x2) ** 2 + (y - y2) ** 2 + (z - z2) ** 2) ** 0.5

            heapq.heappush(min_heap, (distance, data[i], data[j]))
            
            for d in [data[i], data[j]]:
                if d not in uniqueIdsMap:
                    uniqueIdsMap[d] = uniqueIdCounter
                    uniqueIdCounter += 1

    uf = unionfind(uniqueIdCounter) 

    circuits = []
    plannedCircuits = set()     
    for i in range(NUM_CONNECTIONS_TO_MAKE):
        distance, point1, point2 = heapq.heappop(min_heap)
        uf.unite(uniqueIdsMap[point1], uniqueIdsMap[point2])
    
    lenGroups = [len(x) for x in uf.groups()]
    lenGroups.sort()
    lenGroups.reverse()
    print(lenGroups[0] * lenGroups[1] * lenGroups[2])