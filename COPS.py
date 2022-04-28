# cook your dish here
t=int(input())
for _ in range(t):
    m,x,y=map(int,input().split())
    l=list(map(int,input().split()))
    k=x*y
    a=[0 for i in range(100)]
    for i in l:
        lo,hi=i-k,i+k
        if lo<=1:
            lo=1
        if hi>=100:
            hi=100
        for j in range(lo-1,hi):
            a[j]=1
        if a.count(0)==0:
            break
    print(a.count(0))