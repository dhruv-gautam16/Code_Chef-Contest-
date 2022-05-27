for _ in range(int(input())):
    k = int(input())
    if k == 0:
        print(3)
    else:
        ans = '3.'
        t = 103993%33102
        for _ in range(k):
            q = (t*10) // 33102
            r = (t*10) % 33102
            ans += str(q)
            t = r
        print(ans)
    