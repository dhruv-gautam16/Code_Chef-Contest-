# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if (a+b)%2==0:
        print((a+b)//2)
    else:
        print(-1)