import heapq
from unionfind import unionfind

min_heap = []

uniqueIdsMap = {}
uniqueIdCounter = 0

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
    lastPoint1, lastPoint2 = 0, 0  
    while len(uf.groups()) > 1:
        distance, point1, point2 = heapq.heappop(min_heap)
        lastPoint1, lastPoint2 = point1, point2
        uf.unite(uniqueIdsMap[point1], uniqueIdsMap[point2])
        print(len(uf.groups()))
    
    x1 = int(lastPoint1.split(",")[0])
    x2 = int(lastPoint2.split(",")[0])
    print(x1 * x2)