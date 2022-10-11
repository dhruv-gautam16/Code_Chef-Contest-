# cook your dish here

import math

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    x=max(d.values())
    if(x>math.ceil(n/2)):
        print("No")
    else:
        print("Yes")

    