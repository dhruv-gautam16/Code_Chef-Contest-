
for _ in range(int(input())):
    n=int(input())
    d = list(map(int, input().split()))
    tot=ans=0
    for i in range(0,n-1):
        tot+=d[i]
        ans+=abs(tot)

    print(ans)