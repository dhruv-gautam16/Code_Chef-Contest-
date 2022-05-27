# cook your dish here
t=int(input())
while(t):
    t-=1
    n,x,y=map(int,input().split())
    x1=(n+1)//2
    y1=x1 
    if(x1<=x and y1<=y):
        x=x-(y-y1)
        y=y1
        if((x-x1)%2==0):
            print(0)
        else:
            print(1)
    elif(x1<=x and y1>=y):
        x=x-(y1-y)
        y=y1
        if((x-x1)%2==0):
            print(0)
        else:
            print(1)
    elif(x1>=x and y1<=y):
        x=x+(y-y1)
        y=y1
        if((x-x1)%2==0):
            print(0)
        else:
            print(1)
    elif(x1>=x and y1>=y):
        x=x+(y1-y)
        y=y1
        if((x-x1)%2==0):
            print(0)
        else:
            print(1)