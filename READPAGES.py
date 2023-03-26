# cook your dish here
t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    if x*y>=n:
        print("YES")
    else:
        print("No")