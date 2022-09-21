# cook your dish here
#------------------------------------start of template -------------------------------------------------------------------------
# from bisect import bisect_left, bisect_right
from bisect import bisect_left
from heapq import heapify,heappush,heappop
from collections import deque
import sys
from  math import gcd,sqrt,log10,log2,floor,ceil,sqrt
# from  collections import  deque,defaultdict
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
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
for _ in range(ii()):
    n=ii()
    c=il()
    zombie=il()
    ans=[]
    for i in range(n+1):
        ans.append(0)
    for k in range(n):
        low=max(1,k+1-c[k])
        hi=min(n,k+1+c[k])
        ans[low-1]-=1
        ans[hi]+=1
    for l in range(n-1,0,-1):
        ans[l]+=ans[l+1]
    ans1=sorted(ans[1:])
    ans2=sorted(zombie)
    if ans1==ans2:
        print("YES")
    else:
        print("NO")