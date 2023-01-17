# cook your dish here
# cook your dish here
from collections import Counter
t = int(input())
for _ in range(t):
    (n,m) = map(int,input().split())
    a = list(map(int,input().split()))
    ac = Counter(a)
    #print(ac.keys())
    al = list(ac.keys())
    al.sort()
    finlist = []
    for i in range(m-1):
        if i+1 in ac:
            finlist.append(i+1)
    #print(finlist)
    if len(finlist)==m-1:
        if m in ac: print(n-ac[m])
        else: print(n)
    else: print(-1)