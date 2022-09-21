# cook your dish here
t=int(input())
for i in range(t):
    a=int(input())
    x,y,s,f=0,1,0,0
    while s<=a:
        s=x+y
        x=y
        y=s
        if(s==a):
            print("YES")
            f=1
            break
    if(f==0):
        print("NO")