
def solve(a):
	ans = 0
	ele = int(lst[a])
	for i in range(10):
		ans += dp[a][i]*abs(ele - i)
	print(ans)

	



# t = int(input())
 
for _ in range(1):
	
	n, m = list(map(int, input().split()))
	# lst = list(map(int, input().split()))
	lst =  input()

	dp = [[0  for i in range(10)] for j in range(n)]

	for i in range(1, n):
		ele = int(lst[i-1])
		for j in range(10):
			if ele == j:
				dp[i][j] = dp[i-1][j] + 1
			else:
				dp[i][j] = dp[i-1][j]


	for i in range(m):
		a = int(input())
		solve(a-1)