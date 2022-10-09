t = int(raw_input())
for i in range(t):
	C = [[0 for x in range(4)] for y in range(4)]
	N = int(raw_input())
	for k in range(N):
		st = raw_input().split()
		x = int(st[0])
		y = int(st[1])
		if x*y != 0:
			if x > 0:
				if y > 0:
					p = 0
				else:
					p = 1
				# endif
			else:
				if y > 0:
					p = 3
				else:
					p = 2
				# endif
			# endif
			x = abs(x)
			y = abs(y)
			sc = x%2 + 2*(y%2)
			C[p][sc] += 1
		# endif
	# endfor k
	r = 0
	for k in range(4):
		R = [[0 for x in range(8)] for y in range(4)]
		R[0][k] = C[0][k]
		for q in range(1,4):
			for z in range(4):
				tot1 = 0
				tot2 = 0
				for y in range(4):
					if y == z:
						tot2 += R[q-1][y]
						tot1 += R[q-1][y+4]
					else:
						tot1 += R[q-1][y]
						tot2 += R[q-1][y+4]
					# endif
				# endfor y
				R[q][z] = C[q][z]*tot1
				R[q][z+4] = C[q][z]*tot2
			# endfor z
		# endfor q
		for z in range(4):
			if z == k:
				r += R[3][z+4]
			else:
				r += R[3][z]
			# endif
		# endfor z
	# endfor k
	print r
# endfor i

