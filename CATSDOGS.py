# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(x<=y):
        m1=y*4+x*4
        m2=y*4
    elif(x>y and x<=2*y):
        m1=y*4+x*4
        m2=y*4
    else:
        m1=y*4+x*4
        m2=(x-2*y)*4+y*4
    if(z<=m1 and z>=m2 and z%4==0):
        print("yes")
    else:
        print("no")    