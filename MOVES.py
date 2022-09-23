
mod = 1000000007
def integer_list():
	return list(map(int, input().split()))


fact = [0]*(5001)
ifact = [0]*(5001)
fact[0] = 1
ifact[0] = 1
for i in range(1, 5000 + 1):
    fact[i] = (fact[i - 1] * i) % mod
    # inverse(i) = pow(i, mod - 2, mod)
    ifact[i] = (ifact[i - 1] * pow(i, mod - 2, mod)) % mod



def ncr(n, r, p):

	ans =  fact[n]*ifact[r]*ifact[n-r]
	return ans%p

def main():
	try :

		req_right, req_down = n - 1, n -1
		if k%2 == 1:
			#to place right between down = (k -1)//2
			needed_right = (k-1)//2 
			total_places = n - 2
			# distribute identical obj to r person and every one should get least one
			ans = ncr(total_places, needed_right, mod)*ncr(n-2, needed_right, mod)
			print((ans*2)%mod)
		else:
			needed_right = k//2 
			total_places = n - 2
			ans = ncr(total_places, needed_right, mod)*ncr(n-2, needed_right-1, mod)
			print((ans*2)%mod)
	except Exception as e:
		print(e)



# t = int(input())



for _ in range(5000):
	n, k = integer_list()
	ans = 0
	if n == 0 and k == 0:
		break
	main()