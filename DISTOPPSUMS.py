t = int(input())
for _ in range(t):
    n = int(input())
    L = list(range(1,n+1,2))
    R = list(range(2,n+1,2))
    A = L[::-1] + R
    print(*A)