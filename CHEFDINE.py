t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d = dict()
    
    #find min time for each category
    for i in range(n):
        if d.get(a[i],-1) == -1:
            d[a[i]] = b[i]
        else:
            d[a[i]] = min(d.get(a[i],0),b[i])
    
    m = len(d)
    
    if k > m:
        print(-1)
    else:
        ans = sum(list(sorted(d.values())[:k]))
        print(ans)