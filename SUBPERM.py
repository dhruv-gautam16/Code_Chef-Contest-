# cook your dish here
def pro(n,k):
    if(k==1):
        if(n!=1):
            print(-1)
        else:
            print(1)
        return
    arr=[ i for i in range(1,n+1) ]
    k-=2
    arr= arr[:1+k] + arr[1+k:][::-1]
    print(*arr)

n=int(input())
#arr=list(map(int,input().split()))
for i in range(n):
    #n=int(input())
    n,k=list(map(int,input().split()))
    pro(n,k)
