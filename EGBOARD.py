# cook your dish here
from math import ceil
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = [int(x) for x in input().split()]
    # l.sort(reverse = True)
    remBread = 0
    ans = 0
    for i in range(n):
        if l[i]==k:
            ans+=1
            continue
        else:
            if remBread >= l[i]:
                remBread-=l[i]
            else:
                reqBreadPacket = ceil((l[i]-remBread)/k)
                ans+=(reqBreadPacket)
                remBread = (k*reqBreadPacket)-(l[i]-remBread)
            if remBread>0:
                remBread-=1
        # print(ans,remBread)
    print(ans)    