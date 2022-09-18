
def integer_list():
	return list(map(int, input().split()))


def main():
	global lst, n
	lst = [-2] + lst
	lst.append(10**9 + 3)
	lst.sort()
    #all the lst which are nor beautiful 
	lst = [-2] + [lst[i] for i in range(1, n+1) if min(lst[i +1] -lst[i], lst[i] - lst[i-1]) > 1 ]

	lst.append(10**9 + 3)
	
	n = len(lst)
	ans = 0
    #maintain last planted 
	planted = lst[0]
	i = 1
	while i < n-1:
		diff_b = lst[i] - planted
		diff_f = lst[i+1] - lst[i]

		if diff_b == 1 or diff_f == 1:
		    #checking it is already beautiful or not 
			i += 1
		elif diff_f >= 2:
			planted = lst[i] + 1
			i += 1
			ans += 1

		
	print(ans)
		





	
t = int(input())


for _ in range(t):
	n = int(input())
	lst = integer_list()
	main()