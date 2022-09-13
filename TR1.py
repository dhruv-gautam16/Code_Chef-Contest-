

#increase recursion depth other wise it will give error
import sys
sys.setrecursionlimit(100000)

def integer_list():
	return list(map(int, input().split()))

def string_list():
	return list(map(str, input().split()))

def hetro_list():
	return list(input().split())



def dfs(node):
#return childs node with number of direct and indirect child with each branch 
	if node in visited :
		childs_dct[node] = []
		return 0

	childs = dct[node]

	count = []
	s = 0
	visited.add(node)
	for child in childs:
		if child not in visited:
			a = dfs(child) + 1
			s += a
			count.append(a)
		
		
			
	childs_dct[node] = count

	return s

def main():
	try:
		if dct == {}:
			print(1)
			return 
		mod = 1000000007
		dfs(1)
		
		ans = [0]

		for i in range(1, n+1):
			child_list =  childs_dct[i]
			count = 0
			for j in range(len(child_list)):
				a = child_list[j]
				#if we choose parent node as one and other from one brach
				count += (a)*2
				for k in range(j+1, len(child_list)):
				    #choosing from diffrent brach of parent node
					b = child_list[k]
					count += ((a*b))*2
					count %= mod
			ans.append(count+1)
		
		a = 0
		for i in range(n+1):
			a += i*ans[i]
			a %= mod
		print(a)
	except Exception as e:
		print(e)


t = int(input())


for _ in range(t):
	n = int(input())

	dct = {}
	childs_dct = {i: [] for i in range(1, n+1)}
	visited = set()
	for i in range(n-1):
		a, b = integer_list()
		a, b = min(a, b), max(a, b)
		if a not in dct:
			dct[a] = [b]
		else:
			dct[a].append(b)
		if b not in dct:
			dct[b] = [a]
		else:
			dct[b].append(a)


	
	main()
	
	

