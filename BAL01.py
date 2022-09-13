# cook your dish here
from collections import*
for t in range(int(input())):
    s,x = int(input()),list(input())
    cnt=Counter(x)
    for i in range(s):
        if x[i]=='?':
            x[i]='0' if cnt['0']<cnt['1']else '1'
            cnt[x[i]] += 1
    print(''.join(x))        