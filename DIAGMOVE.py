for _ in range(int(input())):
    x,y=map(int,input().split())
    if (abs(x)+abs(y))%2==0:
        print("YES")
    else:
        print("NO")