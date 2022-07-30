# cook your dish here
t = int(input())
while t:
    n,k = map(int,input().split())
    if k == n-1:
        print(-1)
    else:
        for i in range(n-k):
            print((i+1)%(n-k)+1,end=" ")
        for i in range(n-k,n):
            print(i+1,end=" ")
        print()
    t -= 1
#FMREFK