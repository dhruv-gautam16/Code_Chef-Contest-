from sys import stdin
for _ in range(int(stdin.readline())):
	n = int(stdin.readline())
	a = [stdin.readline().strip() for _ in range(n)]
	s = a.pop()
	d = 'Left' if 'Right' in s else 'Right'
	print ( s.replace('Left','Begin').replace('Right','Begin') )
	for ai in a[n-2::-1]:
		d2 = 'Left' if 'Right' in ai else 'Right'
		print ( ai.replace('Left',d).replace('Right',d).replace('Begin',d).replace('Begin',d) )
		d = d2
