for i in range(int(input())):
    n,x,y=map(int,input().split())
    s=2*(n-1)
    d1 = min(x-1,y-1)
    d2 = min(n-x,y-1)
    d3 = min(n-x,n-y)
    d4 = min(x-1,n-y)
    res=s+d1+d2+d3+d4
    print(res)