# cook your dish here
t = int(input())
for _ in range(t):
    n,m,c = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if c%i == 0 and c//i <=m:
            ans += 1
    print(ans)# cook your dish here
