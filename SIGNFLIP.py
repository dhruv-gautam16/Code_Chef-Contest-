
t=int(input())
for i in range(t):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    sm=0
    for k in range(N):
        if A[k]>0:
            sm+=A[k]
    for j in range(K):
        if A[j]<0:
            sm+=A[j]*(-1)
    print(sm)