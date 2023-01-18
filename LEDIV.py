# cook your dish here
# cook your dish here
from math import gcd
from math import sqrt
from functools import reduce
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = reduce(gcd,a)
    if l>1:
        mind = l
        for i in range(2,int(sqrt(l))+1):
            if l%i==0:
                mind = i
                break
        print(mind)
    else: print(-1)