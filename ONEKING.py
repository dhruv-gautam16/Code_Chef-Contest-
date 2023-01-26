t = int(input())
while (t):
    n = int(input())
    kingdoms = []
    for i in range(n):
        kingdoms.append(list(map(int, input().split())))
    kingdoms.sort(key = lambda x : x[1])
    curr = 0
    nex = 1
    bombs = 0
    while (curr<n):
        while (kingdoms[nex][0] <= kingdoms[curr][1]):
            nex += 1
            if (nex == n):
                break
        bombs += 1
        if (nex == n):
            break
        curr = nex
        nex += 1
        if (nex == n):
            bombs += 1
            break
    print(bombs)
    t -= 1
