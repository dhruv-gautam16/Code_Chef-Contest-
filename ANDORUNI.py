# cook your dish here
# cook your dish here

from collections import defaultdict



def AndOrUnion(arr):
    d = defaultdict(lambda: 0)
   # print('&',d)
    for i in arr:
        x = bin(i)[2:]
        for j in range(len(x)):
            if x[j] == '1':
                d[(len(x) - j)] += 1
    s = ''
    for j in range(1, 32):
        if d[j] >= 2:
            s = '1' + s
        else:
            s = '0' + s
    print(int(s, 2))


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    AndOrUnion(arr)