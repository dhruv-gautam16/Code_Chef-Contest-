# cook your dish here
from math import gcd
import sys
inf=10**20
def lcm(a,b):
   return a*b//(gcd(a,b))
for _ in range(int(input())):
    x=int(input())
    ans=inf
    l=list(map(int,input().split()))
    for i in range(x-1):
        for j in range(i+1,x):
            ans=min(ans,lcm(l[i],l[j]))
    print(ans)