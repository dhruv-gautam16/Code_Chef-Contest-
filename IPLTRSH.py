for i in range(int(input())):
    x,y=map(int,input().split())
    if y>x:
        print(0)
    else:
        print(x-y)