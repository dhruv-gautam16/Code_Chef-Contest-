# cook your dish here
t = int(input())
for i in range(t):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    sum = X
    for i in range(N):
        if(A[i]>=0):
            sum = sum + A[i]
            B.append(sum)
        else:
            sum = sum + A[i]
            B.append(sum)
    M = X
    p = max(B)
    print(max(M,p))