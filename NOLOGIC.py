T = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(T):
    q = "".join(input().lower().split())
    s = ''
    for i in q:
        if i in alpha:
            s = s+i
    ans = ''
    for j in alpha:
        if j not in s:
            ans += j
    if len(ans) == 0:
        print('~')
    else:
        print(ans)
    