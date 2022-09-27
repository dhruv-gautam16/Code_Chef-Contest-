# cook your dish here
import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    for i in range(n):
        m=math.gcd(m,abs(l[i]-(i+1)))
    print(m)