t = int(input())
for _ in range(t):
    n = int(input())
    if n%2:
        print(-1)
    else:
        ans = []
        for i in range(1,n+1,2):
            ans.append(i+1)
            ans.append(i)
        print(*ans)
            