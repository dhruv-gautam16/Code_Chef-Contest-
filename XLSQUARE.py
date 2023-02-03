# cook your dish here
import math
t=int(input())
while t>0:
    n,a=map(int,input().split(' '))
    k=math.floor(math.sqrt(n))
    print(a*k)
    t-=1
