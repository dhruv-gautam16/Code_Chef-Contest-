for _ in range(int(input())):
    n, w = list(map(int,input().split()))
    a = [0,] + [-1]*w
    for i in range(n):
        c,p,t = map(int,input().split())
        for j in range(w,t-1,-1):
            if a[j-t]>=0:
                a[j] = max(a[j],a[j-t]+c*p)
    print(max(a))