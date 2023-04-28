for i in range(int(input())):
        s,x,y,z=map(int,input().split())
        if (x+y)+z<=s:
                print("0")
        elif (x+z)<=s or (y+z)<=s:
                print("1")
        else:
                print("2")