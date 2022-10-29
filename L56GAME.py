# cook your dish here
for i in range(int(input())):
	c=0
	N=int(input())
	l=list(map(int,input().split()))
	for i in l:
		if i%2!=0:
		    c+=1
	if c%2==0 or N==1:
	    print(1)
	else:
	    print(2)