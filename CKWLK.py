# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    k = n 
    count = 0
    while k > 0:
        if k//10 == k/10:
            k = k//10
            count += 1
        else:
            break
    p = math.log(k,2)
    if float(p) != math.floor(p):
        print('No')
    else:
        if count < int(p):
            print('No')
        else:
            print('Yes')
            