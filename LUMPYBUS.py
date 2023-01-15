#prevent copy clone duplicate
#Code Protector
# ()..() ()..()
import math
import os,sys
from io import BytesIO, IOBase

for _ in range(int(input())):
    n,p,q=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    res=0
    for i in range(n):
        y,z=0,0
        if (a[i]/2)>=q:
            y=q
            z=q*2
        else:
            y=a[i]//2
            z=y*2
        r=a[i]-z
        if r<=p:
            res+=1
            q-=y
            p-=r
    print(res)