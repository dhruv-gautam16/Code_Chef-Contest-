# cook your dish here
# cook your dish here
# cook your dish here
from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    d=defaultdict(int)
    
    cnt = 0
    for ele in arr:
        if ele == 1:
            if cnt > 0:
                d[cnt] += 1 
            cnt = 0
        else:
            cnt += 1 
    
    
    if cnt > 0:
        d[cnt] += 1 
    
    if len(d.keys()) == 0:
        print('No')
        continue
    
    mx,smax = -1,-1
    for k in d.keys():
        if k > mx:
            smax,mx = mx, k 
        elif k > smax:
            smax = k 
    
    if mx % 2 == 1:
        if d[mx] > 1 or (smax >= mx//2+1):
            print('No')
        else:
            print('Yes')
    else:
        print('No')