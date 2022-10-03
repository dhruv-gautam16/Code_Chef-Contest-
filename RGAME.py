mod = 10**9+7
for t in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    s = ans = 0
    for i in range(1,n+1):
        s = (s + (l[i-1]%mod)*max(2,pow(2,i-1,mod)))%mod
        ans = ((ans*2)%mod + (s*l[i])%mod)%mod
    print(ans)
