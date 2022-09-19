# cook your dish here
t = int(input())



for _ in range(t):
	n = int(input())
	for m in range(1, 30+1):
		x = (2**m)^(2**(m) - 1)
		y = (2**m)^(2**(m)+1)
		if x == n:
			print(2**m - 1)
			break
		elif y == n:
			print(2**m)
			break
	else:
		print(-1)