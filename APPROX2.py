t=int(input())
for j in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=[]
    for i in range(n):
        for j in range(i+1,n):
            z=abs(a[i]+a[j]-k)
            c.append(z)
    r=min(c)
    s=c.count(r)
    print(r,s)