# cook your dish here
st = input().split()
N = int(st[0])
K = int(st[1])
P = int(st[2])
st = input().split()
L = []
for x in range(N):
	n = int(st[x])
	L.append([n,x+1])
# endfor x
L.sort()
H = [0 for x in range(N+1)]
x = L[0][0]
f = L[0][1]
hf = f
H[f] = hf
for k in range(1,N):
	nx = L[k][0]
	f = L[k][1]
	if nx-x > K:
		hf = f
	# endif
	H[f] = hf
	x = nx
# endfor k
for k in range(P):
	st = input().split()
	A = int(st[0])
	B = int(st[1])
	if H[A] == H[B]:
		print ('Yes')
	else:
		print ('No')