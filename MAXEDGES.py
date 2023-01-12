# cook your dish here
import math
# cook your dish here
for _ in range(int(input())):
    n, k, l = map(int, input().split())
    if k+l >= n:
        print((n-k)*(n-l))
    else:
        total = 0
        rem = n-k-l
        total += rem*(k+l) + rem*(rem-1)//2 + k*l
        print(total)
        