# cook your dish here
from collections import *
for _ in range(int(input())):
	r = defaultdict(lambda: [0, 0, 0])
	for _ in range(12):
		ht, hg, _, ag, at = input().split()
		hg = int(hg)
		ag = int(ag)
		r[ht][1] += hg
		r[ht][2] += ag
		r[at][1] += ag
		r[at][2] += hg
		if hg==ag:
			r[ht][0] += 1
			r[at][0] += 1
		elif hg>ag:
			r[ht][0] += 3
		else:
			r[at][0] += 3
	print(*[
	    k
	    for _, _, k in sorted([(-a, c-b, k) for k, [a, b, c] in r.items()])[:2]
	])
