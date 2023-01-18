#prevent copy clone duplicate
#Code Protector
# ()..() ()..()
import math
import os,sys
from io import BytesIO, IOBase

for _ in range(int(input())):
    l,r=map(int,input().split())
    m=1000000007
    x,y=9,1
    while x<l:
        x=x*10+9
        y+=1
    res=0
    while l<=r:
        z=min(x,r)
        p=(((l+z)*(z-l+1))//2)
        res=(res+(y*(p)%m)%m)%m
        l=z+1
        x=x*10+9
        y+=1
    print(res)