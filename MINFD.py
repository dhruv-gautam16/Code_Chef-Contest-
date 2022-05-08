for _ in range(int(input())):
    n,x=map(int,input().split())
    li=list(map(int,input().split()))[:n]
    cnt=0
    sum=0
    while sum<x and len(li)>0:
        sum+=max(li)
        li.remove(max(li))
        cnt+=1
    if sum>=x:
        print(cnt)
    else:
        print(-1)
