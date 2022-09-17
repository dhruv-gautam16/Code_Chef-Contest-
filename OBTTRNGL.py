# cook your dish here
t = int(input())

for i in range(t):
    k, a, b = map(int, input().split())
    c = abs(a - b) - 1
    d = k - c - 2
    s = k & 1
    print(0 if c + 1 == k // 2 and ~s + 2 else min(c, d))