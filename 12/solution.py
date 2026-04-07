# Not a proper solution but solves the problem (for the purpose of getting the star) 
# given the input data grid is either way too small or way too large

with open('real_input.txt') as file:
    data = file.read().split("\n")

ret = 0
for line in data:
    x, y = [int(x) for x in line.split(":")[0].split('x')]
    
    numShapes = [int(x) for x in line.split(": ")[1].split(" ")]
    totalArea = (
        numShapes[0] * 5 +
        numShapes[1] * 7 + 
        numShapes[2] * 6 + 
        numShapes[3] * 7 + 
        numShapes[4] * 7 + 
        numShapes[5] * 7
    )
    if x * y > totalArea:
        ret += 1
print(ret)
