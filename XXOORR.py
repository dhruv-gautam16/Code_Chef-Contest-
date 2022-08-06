import math
def solve(n,k,arr):
	res = 0
	for idx in range(32):
		ans = 0 
		for num in arr:
			ans += (num & pow(2,idx)) > 0
		res += math.ceil(ans/k)
	return res


if __name__ == '__main__':
	for i in range(int(input())):
		n,k = list(map(int,input().split()))
		arr = list(map(int,input().split()))
		print(solve(n,k,arr))
