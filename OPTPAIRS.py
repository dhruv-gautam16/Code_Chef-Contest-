# cook your dish here
from math import sqrt
def snek(x):
    if x == 1:
        return 1
    ans = 2
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            ans += 1
            d = x // i
            if d != i:
                ans += 1
    return ans

t = int(input())

for i in range(t):
    n, = map(int, input().split())
    d = snek(n) - 1
    ans = 2 * d
    if n % 2 == 0:
        ans -= 1
    print(ans)