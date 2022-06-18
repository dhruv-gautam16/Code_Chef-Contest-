# cook your dish here
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    dic = Counter(arr)
    l = dic.items()
    p = []
    for k,v in l:
        p.append(v)
    p.sort()
    print(n-p[-1])