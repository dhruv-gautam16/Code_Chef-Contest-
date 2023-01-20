from math import *

for _ in range(int(input())):
    x, y = map(int, input().split())
    g = gcd(x, y)
    print(x - g)
