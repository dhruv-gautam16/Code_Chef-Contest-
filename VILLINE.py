# cook your dish here
t=int(input())
m,c=map(int,input().split())
a=0
b=0
for j in range(t):
    x,y,p=map(int,input().split())
    d=y-m*x-c
    if(d>0):
        a+=p
    else:
        b+=p
if(a>b):
    print(a)
else:
    print(b)


