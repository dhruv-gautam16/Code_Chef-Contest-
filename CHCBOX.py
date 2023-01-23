for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    x=l1.index(max(l1))
    y=n-l1[::-1].index(max(l1))-1
    if y-x>n//2:
    	print(0)
    else:
    	print(n//2-(y-x))