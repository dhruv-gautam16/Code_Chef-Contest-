for i in range(int(input())):
    w,x,y,z=map(int,input().split())
    if w+y*z>x:
        print("Overflow")
    elif w+y*z<x:
        print("unfilled")
    else:
        print("Filled")