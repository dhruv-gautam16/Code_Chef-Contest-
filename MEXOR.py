#------------------------------------start of template -------------------------------------------------------------------------
from bisect import bisect_left, bisect_right
import math
from bisect import bisect_left
from heapq import heapify,heappush,heappop
from collections import deque
import sys
from  math import gcd,sqrt,log10,log2,floor,ceil,sqrt
from  collections import  deque,defaultdict
input=sys.stdin.readline
# sys.setrecursionlimit(10**6)
def il():
    return [int(a) for a in input().strip().split()]

def ip():
    return input().strip()

def ii():
    return int(input())

def ot(in_p,*args,e=" "):
    if type(in_p)==list:
        print(*in_p,end=e)
    if type(in_p)==str or  type(in_p)==int:
        print(in_p,end=e)
        for l in args:
            print(l,end=e)
    print()
def a_pwr_n(a,n,mod):
    if n==1:
        return a%(mod)
    if n%2==0:
        val=a_pwr_n(a,n//2,mod)
        return val%(mod)*val%(mod)
    else:
        return a%(mod)*a_pwr_n(a,n-1,mod)%(mod)
        
def rg(*ag):
    if len(ag)==3:
        return range(ag[0],ag[1],ag[2])
    elif len(ag)==2:
        return range(ag[0],ag[1])
    elif len(ag)==1:
        return range(ag[0])
    else:
        raise("invalid input")

def ispal(i,j,st):
    while(i<=j):
        if st[i]==st[j]:
            i=i+1
            j=j-1
        else:
            return False
    return True
mod=1000000000+7
dx=[-1,-2,1,2,2,-2,-1,1]
dy=[2,1,2,1,-1,-1,-2,-2]      #knight
#---------------------------------------------end of template ---------------------------------------------------------------------
for i in range(ii()):
    N=ii()
    if N==0:
        print(1)
    else:
        if N==1 or N==2:
            print(2)
        else:
            ans=1
            f=False
            while(ans*2<=N):
                ans*=2
                if ans==N:
                    f=True
                    print(N)
                elif N==(2*ans-1):
                    f=True
                    print(N+1)
            if f==False:
                print(ans)