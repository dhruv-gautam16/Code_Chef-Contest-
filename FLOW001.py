T = int(input())
for tc in range(T):
	
	x=int(input())
	b=str(input())
	a=b.count('C')
	c=b.count('D')
	d=b.count('N')
	if a>d:
		print(60*x)
	elif a==d:
		print(55*x)
	elif d>a:
		print(40*x)
	



	
	