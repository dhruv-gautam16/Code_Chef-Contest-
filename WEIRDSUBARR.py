# cook your dish here
for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    dpl , dpr = [1]*n , [1]*n

    for i in range(1,n):
        if a[i]<a[i-1]:
            dpl[i] += dpl[i-1]
        
    for i in range(n-1,0,-1):
        if a[i-1]<a[i]:
            dpr[i-1] += dpr[i]
        
    ans = 0 

    for i in range (n):
        ans += dpl[i]*dpr[i]
    
    print(ans)
