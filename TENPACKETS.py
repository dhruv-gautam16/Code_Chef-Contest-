# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=5*x
    b=(2*y+x)
    print(min(a,b))