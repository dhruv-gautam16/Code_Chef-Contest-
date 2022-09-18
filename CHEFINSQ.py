
def integer_list():
	return list(map(int, input().split()))

def string_list():
	return list(map(str, input().split()))

def hetro_list():
	return list(input().split())

import math
import sys
from collections import Counter

fact = [0]*51

fact[0] =  1
for i in range(1, 51):
	fact[i] = (fact[i - 1] * i)
	
	

def main():
	lst.sort()
	

	seq = lst[:k]
	dct2 = Counter(seq)
	dct = Counter(lst)
	
	ans = 1
	for ele in dct2:
		ele_req = dct2[ele]
		ele_av = dct[ele]
		ans *= fact[ele_av]//(fact[ele_req]*fact[ele_av - ele_req])
	print(ans)



	



t = int(input())


for _ in range(t):
	n, k = integer_list()
	lst = integer_list()
	main()