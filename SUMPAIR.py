# cook your dish here
for _ in range(int(input())):
    n,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    i = 0
    s = 0
    while i<n-1:
        if a[i]-a[i+1]<d:
            s += a[i]+a[i+1]
            i=i+2
        else:
            i+=1
    print(s)