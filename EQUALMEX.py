# cook your dish here
import collections
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    hash_ = collections.Counter(arr)
    for i in range(n):
        if i in hash_:
            if hash_[i] >= 2:
                continue
            if hash_[i] == 1:
                return "NO"
        else:
            return "YES"
    return "YES"
t = int(input())
while t > 0:
    print(solve())
    t -=1 