for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    new=sorted(a[:])
    r=1
    for i in range(n-1):
        if a[i]>a[i+1]:
            if a[i]+a[i+1]<=x:
               a[i],a[i+1]=a[i+1],a[i]
            else:
                r=0
                break
    if r==1:
        print('YES')
    else:
        print('NO')
        
        
        
