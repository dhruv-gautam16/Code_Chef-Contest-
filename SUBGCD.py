# cook your dish here
from math import gcd

for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    if gcd(*nli)==1:
        print(n)
    else:
        print(-1)