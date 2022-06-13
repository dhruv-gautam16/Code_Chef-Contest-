t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = len(set(a))
    ans = min(n-x, cnt)
    print(ans)