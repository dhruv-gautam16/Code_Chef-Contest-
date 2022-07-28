for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    
    for i in range(1,n):
        a[i]+=a[i-1]
        
    for i in range(n-2, -1, -1):
        b[i]+=b[i+1]
        
    for i in range(n-1):
        ans = max(ans, a[i]+b[i+1])
        
    ans = max(ans,a[n-1])
    ans = max(ans,b[0])

    print(ans)        