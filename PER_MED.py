# cook your dish here
for s in range(int(input())):
	x=int (input())
	p,x2=[],0
	for k in range (1,x+1):
		if k%2==1:
			p.append(x-x2)
			x2+=1
		else:
			p.append(x2)
	print (*p,end=" ");print ()