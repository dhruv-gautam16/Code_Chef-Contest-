# cook your dish here
# cook your dish here
from math import ceil
t = int(input())
for _ in range(t):
    (a,b) = map(int,input().split())
    if a==b: print(0)
    elif b>a:
        print(max(1+ceil((b-1-a)/2),ceil((b-a)/2)))
    elif a>b:
        print(max(ceil((b+1-a)/2),ceil((b-a)/2)))