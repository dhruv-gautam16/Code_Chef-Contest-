for i in range(int(input())):
    x,y,xr,yr,D=map(int,input().split())
    a=x//xr
    b=y//yr
    av=min(a,b)
    if av>=D:
        print("YES")
    else:
        print("NO")
    