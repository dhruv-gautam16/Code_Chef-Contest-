# cook your dish here
T = int(input())
for tc in range(T):
	(n, x) = map(int, input().split(' '))
	
	pizza = n * x // 4
	
	if n*x % 4 == 0:
	    print(pizza)
	else:
	    print(pizza+1)
	