# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x>=y:
        print("yes")
    elif x+z>=y:
        print("yes")
    elif x+2*z>=y:
        print("yes")
    else:
        print("no")