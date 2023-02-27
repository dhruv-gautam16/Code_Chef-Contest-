from collections import Counter
from math import ceil
for i in range(int(input())):
    s=Counter(input().strip())
    r=0
    for i in s:
        r+=ceil(s[i]/2)
    print(r)
