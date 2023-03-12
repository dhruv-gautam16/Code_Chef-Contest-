from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    MOD = 10**9+7
    C = Counter(arr)
    ans = 0
    L = []
    for i in C:
        L.append((i,C[i]))
    L.sort()
    p = 1
    prev = 0
    for i,j in L:
        if i-1==prev:
            p *= j
            ans = (ans + p) % MOD
            prev = i
        else:
            break
    print(ans)