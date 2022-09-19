fib=[1,1]
for i in range(100):
    fib.append(fib[-1]+fib[-2])
from bisect import bisect_left as bl
for _ in range(int(input())):
    n=int(input())
    ind=bl(fib,n)
    if n==1:
        print(1)
    else:
        i=0 
        while i<100 and fib[i]<=n:
            ans=fib[i]
            i+=1 
        print(i-1)