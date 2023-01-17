# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = -(x+y)
    while ans <= 0:
        ans += x*y
    print(ans)