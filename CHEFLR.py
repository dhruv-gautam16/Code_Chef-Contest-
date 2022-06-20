p = 10**9 + 7
t = int(input())
for _ in range(t):
    s = str(input())
    n = len(s)
    ans = 1
    level = 1
    for i in range(n):
        if s[i] == 'l':
            if level%2 == 1:
                ans = (ans*2)
            else:
                ans = (ans*2 - 1)
                
        if s[i] == 'r':
            if level%2 == 1:
                ans = (ans*2 + 2)
            else:
                ans = (ans*2 + 1)
        level += 1
        ans = ans%p
    print(ans)