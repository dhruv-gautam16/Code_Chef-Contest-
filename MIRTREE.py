from math import log
# import sys
from collections import Counter, defaultdict
# from bisect import bisect_left
mod = 1000000007
def integer_list():
	return list(map(int, input().split()))

def string_list():
	return list(map(str, input().split()))

def hetro_list():
	return list(input().split())


# t = int(input())



for _ in range(1):
	n, q = integer_list()
	n = n + 1
	leaf = 2**(n-1)
	total_nodes = 2**n - 1
	edges = total_nodes - 1
	top = 1
	for i in range(q):
		inp = input()
		if len(inp) == 1:
			print(edges%mod)
			continue
		a,b = map(int,inp.split())
		if b == 1 or b == 2:
			edges = 2*edges + n
			leaf = 2*leaf
			top = 2*top
		elif b == 3:

			edges = 2*edges + top
			top = leaf
			n = n*2
		else:
			edges = 2*edges + leaf
			leaf = top
			n = n*2

		
