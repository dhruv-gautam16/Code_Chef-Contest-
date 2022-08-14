# cook your dish here
from collections import Counter
mod=10**9+7
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=dict(Counter(l))
    a=d[max(d.keys())]
    print((pow(2,a,mod)-1)%mod)