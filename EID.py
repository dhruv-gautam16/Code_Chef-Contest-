# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    min = a[1]-a[0]
    for i in range(1,n-1):
        if (a[i+1]-a[i])<min:
            min = a[i+1]-a[i]
    print(min)