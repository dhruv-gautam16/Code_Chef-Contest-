from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    p,q=U()
    try:
        sm=sqrt(p*p+4*q)
        df=sqrt(p*p-4*q)
        b=(sm-df)/2
        a=sm-b
        print(*sorted([a,b,p]),sep=' ')
    except ValueError:
        print(-1)