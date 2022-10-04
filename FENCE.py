# cook your dish here
for _ in range(int(input())):
    m, n, k = [int(x) for x in input().strip().split()]
    g = dict()
    cnt = 0
    for i in range(k):
        r, c = [int(x) for x in input().strip().split()]
        g[r, c] = 0
        cnt += 4
        if((r, c-1) in g):
            cnt -= 2
        if((r, c+1) in g):
            cnt -= 2
        if((r-1, c) in g):
            cnt -= 2
        if((r+1, c) in g):
            cnt -= 2
    print(cnt)