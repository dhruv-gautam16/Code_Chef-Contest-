
t=int(input())
while t!=0:
    n,k=map(int,input().split())
    tot=2*k
    n1=n*15
    if n1>=tot:
        print("YES")
    else:
        print("NO")
    t-=1