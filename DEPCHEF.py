# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = [int(i) for i in input().split()]
    best = -1
    if d[0] > a[-1] + a[1]:
        best = d[0]
    for i in range(1,n-1):
        if d[i] > a[i-1] + a[i+1] and d[i] > best:
            best = d[i]
    if d[n-1] > a[n-2] + a[0] and d[n-1] > best:
        best = d[n-1]
    print(best)