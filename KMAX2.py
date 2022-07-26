t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = max(a)
    count = 0
    for j in range(0, len(a)):
        if a[j] == d and j >= k-1:
            count+=(n-j)
    print(count)