for _ in range(int(input())):
    x, y = map(int, input().split())
    if x<y:
        print(y-x)
    else:
        if (x-y)%2==0:
            print((x-y)//2)
        else:
            print((x-y)//2+2)
    
