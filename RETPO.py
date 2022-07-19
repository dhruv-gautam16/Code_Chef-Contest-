for t in range(int(input())):
    x,y=list(map(int,input().split()))
    x = abs(x)
    y = abs(y)
    t=x+y
    if(x==y):
        print(t)
    elif(x>y):
        if(t%2==0):
            print(2*x)
        else:
            print(2*x + 1)
    else:
        if(t%2==0):
            print(2*y)
        else:
            print(2*y - 1)
        