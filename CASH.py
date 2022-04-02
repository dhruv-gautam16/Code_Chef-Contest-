from math import gcd
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += (ar[i] % k) 
    print(ans % k)