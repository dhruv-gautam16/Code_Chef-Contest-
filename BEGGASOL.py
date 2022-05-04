for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))[:n]
    gasoline=li[0]
    cnt=0
    for i in range(1,n):
        if gasoline==0:
            break
        gasoline-=1
        cnt+=1
        gasoline+=li[i]
    print(gasoline+cnt)
