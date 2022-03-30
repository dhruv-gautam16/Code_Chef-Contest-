t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    for i in range(n-k,n+1):
        print(i,end=" ")
    for i in range(1,n-k):
        print(i,end=" ")