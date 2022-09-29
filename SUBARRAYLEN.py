# cook your dish here
t=int(input())
for i in range(t) :
    n=int(input())
    m=n+1
    a=list(map(int,input().split()))
    p=[[-1] for i in range(m)]
    for i in range(n) :
        p[a[i]] += [i]
    a= (n * (m)) //2
    for i in range(1,m):
        p[i]+=[n]
        a -= sum(max(0,p[i][j+1]-p[i][j]-i)for j in range(len(p[i])-1))
    print(a)