# cook your dish here
t=int(input())
while t!=0:
    n=int(input())
    h=list(map(int,input().split()))
    g=list(map(int,input().split()))
    f=b=1
    for j in range(0,n):
        if f==1 or b==1:
          if h[j]>g[j]:
            f=0
          if h[j]>g[n-1-j]:
            b=0
    if f==1 and b==1:
        print("both")
    elif f==1:
        print("front")
    elif b==1:
        print("back")
    else:
        print("none")
    t-=1