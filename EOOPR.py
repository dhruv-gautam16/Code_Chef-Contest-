for _ in range(int(input())):
    x,y = map(int,input().split())
    if y==x:
        print(0)
    elif y>x and (y-x)%2==1:
        print(1)
    elif y>x and (y-x)%4==0:
        print(3)
    elif y>x and (y-x)%2==0:
        print(2)
    elif y<x and (x-y)%2==0:
        print(1)
    elif y<x and (x-y)%2==1:
        print(2)