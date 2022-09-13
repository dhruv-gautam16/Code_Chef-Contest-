# cook your dish here

def integer_list():
	return list(map(int, input().split()))

def string_list():
	return list(map(str, input().split()))

def hetro_list():
	return list(input().split())





import math	

from collections import Counter


def solve():

	#∣V∣≥K  the winner is Vanja; 


	v1 = 0
	for i, v in enumerate(lst):
		if i%2 == 0:
			if v1 < 0:
				v1 -= v
			else:
				v1 += v
		else:
			if v1 > 0:
				v1 -= v
			else:
				v1 += v
	if abs(v1) >= k:
		print(1)
	else:
		print(2)



t = int(input())

for _ in range(t):
	n, k = integer_list()
	lst = integer_list()
	solve()