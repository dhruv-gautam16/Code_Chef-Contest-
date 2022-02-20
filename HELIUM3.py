T = int(input())
for tc in range(T):
	
	(a, b,x,y) = map(int, input().split(' '))
	if(a*b<=x*y):
		print('yes')
	else:
		print('No')