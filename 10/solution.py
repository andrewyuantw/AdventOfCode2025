def serializeArray(arr):
    ret = ""
    for c in arr:
        if c:
            ret += "."
        else:
            ret += "#"
    return ret

with open('real_input.txt') as file:
    data = file.read().split("\n")
    ret = 0
    for line in data:
        d = line.split(" ")
        buttons = []
        for c in d:
            if c[0] == '[':
                puzzleToSolve = [True if x == '.' else False for x in c[1:-1]]
                
            if c[0] == '(':
                buttons.append([int(x) for x in c[1:-1].split(',')])
        # Do BFS exploration
        bfs = [(0, [True] * len(puzzleToSolve))]
        visited = set()
        visited.add(serializeArray([True] * len(puzzleToSolve)))
        while True:
            currStep, currState = bfs.pop(0)
            if currState == puzzleToSolve:
                ret += currStep
                break
            for button in buttons:
                newState = currState.copy()
                for i in button:
                    newState[i] = not newState[i]
                if serializeArray(newState) not in visited:
                    bfs.append((currStep + 1, newState))
                    visited.add(serializeArray(newState))

    print(ret)