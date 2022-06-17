# cook your dish here
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    req = []
    for i in range(n):
        req.append(input())
    p = list(set(req))
    k = len(p)
    if k == 0:
        print('Draw')
    elif k == 1:
        print(p[0])
    else:
        t1 = 0
        t2 = 0
        for i in req:
            if i == p[0]:
                t1 += 1 
            else:
                t2 += 1 
        if t1 > t2:
            print(p[0])
        elif t1 == t2:
            print('Draw')
        else:
            print(p[1])