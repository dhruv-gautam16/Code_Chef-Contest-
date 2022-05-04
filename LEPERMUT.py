T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    p = 0
    l = 0
    for i in range(N-1):
        if A[i] > A[i+1]:
            p += 1
    
    for i in range(N):
        for j in range(i+1,N):
            if A[i]>A[j]:
                l += 1
    if p == l:
        print('YES')
    else:
        print('NO')