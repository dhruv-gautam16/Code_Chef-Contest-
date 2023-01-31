def solve():
	B = []
	B.append([0,0,-1,-1])
	sz = 1
	M = int(input())
	for k in range(M):
		D = {}
		D[1] = 0
		N = int(input())
		for x in range(N-1):
			st = input().split()
			p = int(st[0])
			dr = st[1]
			c = int(st[2])
			p = D[p]
			d = B[p][0]
			if dr == 'L':
				q = B[p][2]
				if q == -1:
					q = sz
					B[p][2] = sz
					sz += 1
					B.append([d+1,0,-1,-1])
			else:
				q = B[p][3]
				if q == -1:
					q = sz
					B[p][3] = sz
					sz += 1
					B.append([d+1,0,-1,-1])
			D[c] = q
			B[q][1] += 1
	R = [0 for x in range(1000)]
	for p in range(1,sz):
		d = B[p][0]
		n = B[p][1]
		if n > R[d]:
			R[d] = n
	st = ''
	p = 1000
	m = 0
	while p > 1:
		p -= 1
		if R[p] > m:
			while R[p] > m:
				st += str(p) + ' '
				m += 1
	while m < M:
		st += '0 '
		m += 1
	print (st)

for i in range(int(input())):
    solve()