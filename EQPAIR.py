# cook your dish here
t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split(" ")))
    d = {}
    for i in range(n):
        if d.get(a[i]):
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for each in d:
        if d[each]>1:
            ans += ((d[each]-1)*(d[each]))//2
    print(ans)
    t -= 1