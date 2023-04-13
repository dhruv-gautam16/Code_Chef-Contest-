for t in range(int(input())):
    x,y = map(int,input().split())
    if(y*100 <= x*107 ):
        print("Yes")
    else:
        print("No")