
for _ in range(int(input())):
    x,y=map(int,input().split())
    if y-x<x:
        print(y)
    else:
        print(-1)