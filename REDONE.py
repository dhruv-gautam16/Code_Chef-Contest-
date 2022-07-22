# import math
q = 1000002
f =[1]
mod = 1000000007 
for i in range(1,q):
    f.append((f[-1]*i)%mod)
for _ in range(int(input())):
    n=int(input())
    print(f[n+1]-1)
    