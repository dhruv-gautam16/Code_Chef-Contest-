from math import log
# import sys
from collections import Counter, defaultdict
# from bisect import bisect_left
# mod = 1000000007
def integer_list():
	return list(map(int, input().split()))

def string_list():
	return list(map(str, input().split()))

def hetro_list():
	return list(input().split())


t = int(input())



for _ in range(t):
	n, m = integer_list()
	min_salary = integer_list()#min salary required 
	offered_salary = []
	maxjob_offers = []
	for i in range(m):
		a, b = integer_list()
		offered_salary.append(a)
		maxjob_offers.append(b)
	qual = [ list(map(int,list(input()))) for i in range(n)]
	#qual[i][j] ith candidate in j tht company
	candidates_with_job = 0
	total_salaries = 0
	visited = set()

	for s in range(n):
		expected = min_salary[s]
		comp, sal = -1, -1
		for j in range(m):
			offered = offered_salary[j]
			if offered >= expected and qual[s][j] and maxjob_offers[j]:
				if offered > sal:
					comp = j
					sal = offered

		if comp != -1:
			maxjob_offers[comp] -= 1
			visited.add(comp)
			total_salaries += sal
			candidates_with_job += 1
	print(candidates_with_job, total_salaries, m - len(visited))

			
