# cook your dish here
from math import gcd
t=int(input())
for j in range(t):
    a,b=map(int,input().split())
    if(a<2 or b<2):
        print(-1)
    elif(gcd(a,b)==1):
        print(1)
    else:
        print(0)
    
