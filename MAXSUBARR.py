# cook your dish here
# cook your dish here
for _ in range(int(input())):
    N = int(input()); A = list(map(int, input().split())); M = int(input()); B = list(map(int, input().split())); mx = float('-inf'); curmax = 0; curmax2 = 0; stmx = -1; enmx = -1;
    for i in range(N):
        curmax += A[i]; curmax2 += A[-i - 1]
        if curmax > mx: mx = curmax
        if i == (N - 1): enmx = curmax; stmx = curmax2
        if curmax < 0: curmax = 0
        if curmax2 < 0: curmax2 = 0
    z = sum([x for x in B if x > 0]); print(max(z, z + stmx, z + enmx, mx))
