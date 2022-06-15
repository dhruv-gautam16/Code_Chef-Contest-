# cook your dish here
from collections import defaultdict as df
for _ in range(int(input())):
    n=int(input())
    d=df(int)
    for i in range(n):
        s=input()
        m=len(s)
        mp=df(int)
        for j in range(m):
            mp[s[j]]=1
        for k in mp:
            d[k]+=1
    ans=0
    for i in d:
        if d[i]==n:
            ans+=1
    print(ans)
