# cook your dish here
from itertools import combinations 
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    a=l[0]
    b=l[1]
    n = b-a+1
    k=b-a-1
    result=(n*(n+1))//2
    extra=(k*(k+1)//2)
    print(result-extra)