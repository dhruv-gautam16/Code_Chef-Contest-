# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mod = 0
    for i in range(n-1):
        if(a[i]%a[i+1]>a[i+1]%a[i]):
            mod = a[i]%a[i+1]
            a[i+1] = mod
        else:
            mod = a[i+1]%a[i]
            a[i+1] = mod
    print(mod)