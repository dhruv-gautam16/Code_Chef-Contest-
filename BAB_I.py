for i in range(int(input())):
    a = int(input())
    l = list(map(int, input().split(" ")))
    for i in range(a):
        l[i] = abs(l[i])
    l.sort()
    if l[0] == 0:
        print(-1)
    else:
        print(l[0]-1)