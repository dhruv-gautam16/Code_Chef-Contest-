for i in range(int(input())):
	n=int(input())
	a=list(map(int, input().split()))
	c=0
	x=0
	for i in range(n):
		if a[i] in range(1,8):
			c+=1
		if c==7:
			x=i+1
			break
	print(x)