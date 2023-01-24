import math
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    print(math.ceil(math.log(max(Counter(a).values()), 2)))
    # 2 2 2 2 2
    
    # 3 3 3 2 2
    # 5 5 3 4 4
    # 5 8 3 7 4