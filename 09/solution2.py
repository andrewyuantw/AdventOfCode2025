from functools import cache
import time
start = time.time()

with open('real_input.txt') as file:
    data = file.read().split("\n")

# map integers down to lower space
coords = [tuple(int(v) for v in d.split(",")) for d in data]
xs = sorted(set(x for x, _ in coords))
ys = sorted(set(y for _, y in coords))
    
xMapLargeToSmall = {x: i for i, x in enumerate(xs)}
xMapSmallToLarge = {i: x for i, x in enumerate(xs)}
yMapLargeToSmall = {y: i for i, y in enumerate(ys)}
yMapSmallToLarge = {i: y for i, y in enumerate(ys)}
    
mappedData = [(xMapLargeToSmall[x], yMapLargeToSmall[y]) for x, y in coords]
edges = [(mappedData[i], mappedData[(i + 1) % len(mappedData)]) for i in range(len(mappedData))]

def isOnPolygonEdge(pointOfInterest, vertex1, vertex2):
    x, y = pointOfInterest
    x1, y1 = vertex1
    x2, y2 = vertex2
    # Vertical edge
    if x1 == x2 and x == x1 and y >= min(y1, y2) and y <= max(y1, y2):
        return True
    # Horizontal edge
    if y1 == y2 and y == y1 and x  >= min(x1, x2) and x <= max(x1, x2):
        return True
    return False

@cache
def isPointInPolygon(x, y):
    numIntersections = 0
    for (x1, y1), (x2, y2) in edges:
        if isOnPolygonEdge((x, y), (x1, y1), (x2, y2)):
            return True
        # raycast to the right and count intersections
        if x1 == x2 and x1 > x and min(y1, y2) < y + 0.5 < max(y1, y2):
            numIntersections += 1
    return numIntersections % 2 == 1

ret = 0
for i in range(len(mappedData)):
    print(i)
    for j in range(i + 1, len(mappedData)):
        x, y = mappedData[i]
        a, b = mappedData[j]
        potentialArea = (abs(xMapSmallToLarge[x] - xMapSmallToLarge[a]) + 1) * (abs(yMapSmallToLarge[y] - yMapSmallToLarge[b]) + 1)
        if potentialArea > ret:
            # Try each point on all four edges of the potential rectangle
            all_points_of_edge_in_polygon = (
                all(isPointInPolygon(z, r) for z in range(min(x, a), max(x, a)) for r in [y, b]) and
                all(isPointInPolygon(z, r) for z in [x, a] for r in range(min(y, b), max(y, b)))
            )
                        
            if all_points_of_edge_in_polygon:
                ret = potentialArea
print(ret)
print(f"Elapsed: {time.time() - start:.2f}s")
