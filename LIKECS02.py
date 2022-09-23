
def main():
	try :
		#possible sum of all terms = n**2, n*(n-1), n*(n+ 1)
		if n%2 == 1:
			#possible mid term == n -1, n,n+1
			#value    n**2 <=  s <= n*(n +1)
			i = n - 1
			j = n + 1
			lst = [n]
			for k in range(n//2):
				lst.append(i)
				lst.append(j)
				i -= 1
				j = j + 1
			lst.sort()
			print(*lst)

		else:
			#possible mid terms sum= 2n-2, 2n, 2n + 2
			i = n - 1
			j = n + 1
			lst = [i , j]
			for k in range((n-2)//2):
				i -= 1
				j = j + 1
				lst.append(i)
				lst.append(j)
			lst.sort()
			print(*lst)

	except Exception as e:
		print(e)



t = int(input())



for _ in range(t):
	n = int(input())
	
	main()


	

