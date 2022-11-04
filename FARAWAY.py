t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    r=[]
    for j in l:
        ma=0
        ma=max((j-1),(m-j))
        r.append(ma)
    print(sum(r))
