# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    for i in a:
        c = c | i
    ans = 0
    for i in a:
        ans = ans | (i^c)
    print(c,ans)