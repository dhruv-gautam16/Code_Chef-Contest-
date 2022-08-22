# cook your dish here
t = int(input())

for i in range(t):
    k = int(input())
    m = (int)(1e9 + 7)
    a = 10
    r = 2
    s = a * pow(r, (k - 1), m)
    ans = s % m
    print(ans)