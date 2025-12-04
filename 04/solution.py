def isInBounds(x, y, grid):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])



def getRolls(grid, debugGrid):
    ret = 0
    diffs = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '@':
                count = 0
                for dx, dy in diffs:
                    newX, newY = x + dx, y + dy
                    if isInBounds(newX, newY, grid) and grid[newX][newY] == '@':
                        count += 1
                if count < 4:
                    ret += 1
                    
                    debugGrid[x][y] = 'x'
    return ret


with open('input.txt') as file:
    data = file.read()
    grid = data.split("\n")

    debugGrid = [list(row) for row in data.split("\n")]

    
    print(getRolls(grid, debugGrid))

    for row in debugGrid:
        print("".join(row))

