# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    if(x==w)or(y==w)or(z==w):
        print("yes")
    elif(x+y==w)or(x+z==w)or(y+z==w):
        print("yes")
    elif(x+y+z==w):
        print("yes")
    else:
        print("no")
