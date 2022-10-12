t = int(raw_input())
for i in range(t):
	N = int(raw_input())
	if N < 4:
		print '-1'
	else:
		st = ''
		p = 2
		while p <= N:
			st += str(p) + ' '
			p += 2
		# endwhile
		p = 1
		while p <= N:
			st += str(p) + ' '
			p += 2
		# endwhile
		print st
	# endif
# endfor i

