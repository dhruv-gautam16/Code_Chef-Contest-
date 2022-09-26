import math
import sys
from collections import Counter, defaultdict
from bisect import bisect_left
mod = 1000000007
def integer_list():
	return list(map(int, input().split()))





def main():
	try : 
		
		new_lst = [0] + lst
		lst_sum = sum(lst)
		if lst_sum%n != 0:
			print(-1)
			return 
			
		needed_sum = lst_sum//n
		count = 0
	
		for i in range(1, n-d + 1):
			if new_lst[i] < needed_sum:
				count += needed_sum - new_lst[i]
				new_lst[i+d] -= needed_sum - new_lst[i]
				new_lst[i] = needed_sum
				
			else:
				count += new_lst[i] - needed_sum
				new_lst[i+d] += new_lst[i] - needed_sum
				new_lst[i] = needed_sum
				
		for i in range(1, n+1):
			if new_lst[i] != needed_sum:
				print(-1)
				break
		else:
			print(count)

		
	except Exception as e:
		print(e)



t = int(input())



for _ in range(t):
	n, d= integer_list()
	lst = integer_list()
	
		
	main()
