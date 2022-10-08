a=1000000007
while(True):
	N=int(input())
	if(N==0):
	    break
	v=list(map(int,input().split()))
	len=(1<<N)-1
	for i in range(len//2,-1,-1):
		left=i*2+1;right=i*2+2
		if(left<len and right<len): 
		    v[i]=v[i]*max(v[left],v[right]);
		elif(left<len):
		    v[i]=v[i]*v[left]
	print(v[0]%a)