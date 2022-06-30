
n,m = [int(i) for i in input().split()]
for i in range(m):
    q = int(input())
    if q<=3*n and q>=n+2:
        x = n+2
        mx = n
        ans = abs(x-q)+1
        if ans> mx:
            ans = mx-(ans-mx)
    else:
        ans=0
    print(ans)