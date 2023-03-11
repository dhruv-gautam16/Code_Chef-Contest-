# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    a,b,c = 1,0,0
    chk = 2
    while chk < math.sqrt(n):
        if n % chk:
            chk += 1
        else:
            b = chk
            break
    if b == 0:
        print(-1)
    else:
        c = n // b
        print(a,b,c)