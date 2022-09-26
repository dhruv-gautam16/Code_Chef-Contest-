# cook your dish here
ri = lambda : int(input())
rl = lambda : list(map(int,input().split()))
rs = lambda : input()
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def gcd(x,y):
    while y>0:
        x,y=y,x%y 
    return x
t=ri()
for test in range(t):
    n,q=rl()
    arr=rl()
    prefix=[0]*(n+2)
    suffix=[0]*(n+2)
    for i in range(n):
        prefix[i+1]=gcd(prefix[i],arr[i])
    for i in range(n,0,-1):
        suffix[i]=gcd(suffix[i+1],arr[i-1])
    for i in range(q):
        l,r=rl()
        ans=gcd(prefix[l-1],suffix[r+1])
        print(ans)
    
    
    
   