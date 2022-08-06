# cook your dish here
mod = 1000000007
t = int(input())
for tc in range(t):
    n = int(input())
    ans = pow(3,n,mod)
    if n%2 == 0:
        ans = (ans+3)%mod
    else:
        ans = (ans-3)%mod
        
    print(ans)