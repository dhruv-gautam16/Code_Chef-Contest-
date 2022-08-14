import sys

q = []
visited = {}
backTrack = {}
goalState = [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0]

rotations = {
    0 : {
        'R' : [0, 2, 5, 8, 6, 3],
        'L' : [0, 3, 6, 8, 5, 2],
    },
    1 : {
        'R' : [1, 3, 6, 9, 7, 4],
        'L' : [1, 4, 7, 9, 6, 3],
    },
    2 : {
        'R' : [6, 8, 10, 12, 11, 9],
        'L' : [6, 9, 11, 12, 10, 8],
    },
}

def getHashKey(state):
    h = 0
    for i in range(13):
        h = h * 2 + int(state[i])
    return h

def printSolution(key):
    target = key
    cnt = 0
    l = []
    while key != 600:
        cnt += 1
        key, no, direction, state = backTrack[key]
        direction = 1 if direction == 'L' else 0
        l.append((no, direction))

    print cnt
    for no, direction in l:
        print no, direction

def solve(key):
    startKey = key

    if len(q) == 0:
        q.insert(0, goalState)

    while len(q) > 0:
        state = q.pop()
        sKey = getHashKey(state)
        found = 0
        for rstate, no, direction in rotate(state):
            rKey = getHashKey(rstate)
            
            if rKey == startKey:
                found = 1

            if not visited.has_key(rKey):
                visited[rKey] = True
                backTrack[rKey] = (sKey, no, direction, state)
                q.insert(0, rstate)

        if found:
            printSolution(startKey)
            return

def rotate(state):
    for no in range(3):
        for direction in ['L', 'R']:
            result = state[:]
            rot = rotations[no][direction]
            prev = 0
            tmp = result[rot[prev]]
            for cur in range(1, 6):
                result[rot[prev]] = result[rot[cur]]
                prev = cur
            result[rot[prev]] = tmp
            yield result, no, direction

noTestCases = int(sys.stdin.readline().rstrip())
while noTestCases > 0:
    noTestCases -= 1
    state = sys.stdin.readline().rstrip()
    key = getHashKey(state)
    if backTrack.has_key(key):
        printSolution(key)
    else:
        solve(key)

