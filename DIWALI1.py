t=int(input())
for j in range(t):
    p,a,b,c,x,y=map(int,input().split())
    r=b+x*a
    s=c+y*a
    v=min(r,s)
    print(p//v)