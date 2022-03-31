t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if (abs(x+z)>y):
        print("No")
    else:
        print("Yes")
