import sys
from math import sqrt,gcd,factorial,ceil,floor,pi
from collections import deque,Counter,OrderedDict
from heapq import heapify,heappush,heappop
sys.setrecursionlimit(10**6)
input =lambda: sys.stdin.readline()
I     =lambda :int(input())
S     =lambda :input().strip()
M     =lambda :map(int,input().strip().split())
L     =lambda :list(map(int,input().strip().split()))
mod=10**9+7 

##########################################################


def dfs(node):
	st = [node]
	v[node] = 1
	ans = 0
	while st:
		cur = st.pop()
		ans+=1
		for i in adj[cur]:
			if not v[i]: st.append(i);v[i] = 1
	return ans
	
for _ in range(I()):
	n,m = M()
	adj = {i+1: [] for i in range(n)}
	for i in range(m):
		p,q = M()
		adj[p].append(q)
		adj[q].append(p)

	v = [0]*(n+1)
	a1,a2 = 0,1
	for i in range(n):
		if not v[i+1]:
			a1+=1
			a2*=dfs(i+1)
			a2%=mod
	print(a1,a2)