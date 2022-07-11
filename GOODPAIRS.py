# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sample = {}
    ans = 0
    for i in range(n):
        if (b[i],a[i]) in sample:
            ans += sample[(b[i],a[i])]
            if (a[i],b[i]) in sample:
                sample[(a[i],b[i])] += 1 
            else:
                sample[(a[i],b[i])] = 1 
        else:
            if (a[i],b[i]) in sample:
                sample[(a[i],b[i])] += 1 
            else:
                sample[(a[i],b[i])] = 1 
            
    print(ans)
        