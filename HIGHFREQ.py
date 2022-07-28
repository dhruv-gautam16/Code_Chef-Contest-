# cook your dish here
from collections import Counter
import math
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c = Counter(arr)
    x= list(c.values())
    x.sort(reverse=True)
    if(len(x)==1):
        print(math.ceil(x[0]/2))
    else:
        print(max(math.ceil(x[0]/2),x[1]))