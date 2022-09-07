def solve():
	
	transfored = [0] + [ ele for ele in range(1, n+1) if ele%2 == 0] + [ ele for ele in range(1, n+1) if ele%2 == 1]

	

	visited = [False] * (n+1)	
	count = 0 
	for i in range(1, n+1):
		
		if not visited[i]:
			temp = i 
			while not visited[temp]:
				visited[temp] = True 
				temp = transfored[temp]
			count += 1 
			
	
	print((26**count)%mod) 

t = int(input())

for _ in range(t):
	mod = 10**9 + 7
	n = int(input())
	solve()
