# cook your dish here

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x-y<=0:
        print(x)
    else:
        print(x-y+x)
        
        