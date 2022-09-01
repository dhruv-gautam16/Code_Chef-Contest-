# cook your dish here
for _ in range(int(input())):
    n, k, s = map(int, input().split())
    tot = k*s
    opend = s-(s//7)
    if tot > n * opend or (s >= 7 and (n-k)*6 < k):
        print(-1)
    else:
        ans = tot//n
        if tot%n != 0:
            ans+=1
        print(ans)
