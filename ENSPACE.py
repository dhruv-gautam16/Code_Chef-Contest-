# cook your dish here
t=int(input())
for t in range(t):
    n,x,y=map(int,input().split())
    if(x+2*y<=n):
        print('yes')
    else:
        print("no")