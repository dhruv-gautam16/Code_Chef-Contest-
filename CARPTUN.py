#prevent copy clone duplicate
#Code Protector
# ()..() ()..()
import math
import os,sys
from io import BytesIO, IOBase


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c,d,s=map(int,input().split())
    print(float((c-1)*max(a)))