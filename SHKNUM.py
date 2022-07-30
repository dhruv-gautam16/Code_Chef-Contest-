# cook your dish here
from bisect import bisect, insort

def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo

def find_le(a, x):
    # 'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError
    
def find_gt(a, x):
    # 'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

possible_m = []

for i in range(31):
    for j in range(31):
        if i != j:
            possible_m.append((2 ** i) + (2 ** j))
possible_m = sorted(possible_m)

t = int(input())
for i in range(t):
    n = int(input())
    if n < 3:
        print(3 - n)
    else:
        print(min((n - find_le(possible_m, n)), find_gt(possible_m, n) - n))