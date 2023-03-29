t=int(input())
for i in range(t):
    x,p,q=map(int,input().split())
    if p>q:
        a=p-q
        print(a*x)
    else:
        print(0)