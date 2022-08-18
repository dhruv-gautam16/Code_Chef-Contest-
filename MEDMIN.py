# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    x = (n+1)//2
    if x%2:
        # print(x,l)
    	print(abs(l[x-1]-l[x-2]))
    # 	print(l)
    else:
      	print(abs(l[x-2]-l[x-1]))
    
    