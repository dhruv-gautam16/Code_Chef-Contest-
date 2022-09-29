for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    d=n+m
    if x%2==d%2 or y%2==d%2:
        print("Yes")
    else:
        print("No")
    
        