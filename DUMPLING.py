from math import gcd
import sys

for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    g = gcd(a, b)
    f = gcd(c, d)
    d = k//(g * f // gcd(g, f))
    print(2*d + 1)