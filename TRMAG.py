
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    r=int(input())
    s,t=(n*(n+1))/2,(n+1)//2
    for i in range(1,a[0]+1):
        s-=a[i]
    s=(s*(t-r))/t
    print("%.4f"%(s))
    