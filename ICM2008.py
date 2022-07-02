for _ in range (int(input())):
    a, b, c, d=map(int,input().split())
    dis=abs(a-b)
    effSpd=abs(c-d)
    if (a==b):
        print("YES")
    else:
        if (c==d):
            print("NO")
        else:
            time=dis/effSpd
            if (time-int(time)==0):
                print("YES")
            else:
                print("NO")
    