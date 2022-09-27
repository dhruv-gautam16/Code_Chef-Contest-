# cook your dish here
MD = 1000000007
P = [[0 for x in range(1001)] for y in range(1001)]
P[1][1] = 1
for n in range(2,1001):
	for w in range(1,n+1):
		P[n][w] = (P[n-1][w-1] + w*P[n-1][w])%MD
	# endfor w
# endfor n
t = int(input())
for i in range(t):
	N = int(input())
	tot = 0
	for w in range(1,N+1):
		tot += P[N][w]
	# endfor w
	r = tot%MD
	print (r)
    