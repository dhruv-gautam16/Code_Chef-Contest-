# cook your dish here
from math import ceil
for tc in range(int(input())):
    p0,p1=map(int,input().split())
    
    x0=ceil(p0/9)
    x1=ceil(p1/9)
    
    if x0>=x1:
        print(1,x1)
    
    else:
        print(0,x0)
    