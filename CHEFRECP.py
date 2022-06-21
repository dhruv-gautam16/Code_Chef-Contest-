# cook your dish here
from collections import Counter
t = int(input())
for _ in range(t):
    flag = False
    n = int(input())
    arr = [int(i) for i in input().split()]
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            if arr[i-1] in arr[i:]:
                flag = True
                break
    if flag:
        print('NO')
    else:
        dic = Counter(arr)
        l = list(dic.values())
        if len(l) != len(set(l)):
            print('NO')
        else:
            print('YES')