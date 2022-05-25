T=int(input())
for i in range(T):
	N,K=map(int,input().split())
	c=0
	for j in range(1,K+1):
		rem=N%j
		if rem>c:
			c=rem
	print(c)