# cook your dish here
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            arr[i] = 0
    dic = Counter(arr)
    l = list(dic.items())
    l.sort(key = lambda x : (-x[1],x[0]))
    if l[0][0] == 0:
        print(l[1][0])
    else:
        print(l[0][0])