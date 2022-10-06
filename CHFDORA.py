# cook your dish here
# cook your dish here
def snek(s, j, k):
    x = 1
    c = 0
    while j - x >= 0 and j + x < n and k - x >= 0 and k + x < m:
        if s[j - x][k] == s[j + x][k] and s[j][k - x] == s[j][k + x]:
            c += 1
            x += 1
        else:
            break
    return(c)
    
t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    s = []
    ans = 0
    for i in range(n):
        s.append(list(map(int, input().split())))
    for j in range(1, n):
        for k in range(1, m):
            ans += snek(s, j, k)
    print(n * m + ans)