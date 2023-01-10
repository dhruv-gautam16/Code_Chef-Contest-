# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ma = 0
    count = 1
    for i in range(1,n):
        if a[i]^a[i-1]<=1:
            count+=1
        else:
            ma = max(ma, count)
            count=1
    ma = max(ma, count)
    print(n-ma)