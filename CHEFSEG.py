# cook your dish here
import math


for _ in range(int(input())):
    x,k=map(int,input().split())
    y=int(math.log2(k))
    z=2**y
    m=k-z
    ans=(2*m+1)*(x)/(2**(y+1))
    print(ans)
