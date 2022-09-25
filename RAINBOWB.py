def ilist():
    return list(map(int,input().split()))
def iint():
    return map(int,input().split())
def lemptylist(n):
    ans=[]
    for i in range(n):
        ans.append([])
    return ans
MAXN = 10**6 + 10
mod = 10**9 + 7

fac = [i for i in range(MAXN)]
fac[0] = 1
for i in range(1, MAXN):
	fac[i] *= fac[i-1]
	fac[i] %= mod

ifac = [0 for i in range(MAXN)]
ifac[-1] = pow(fac[-1], mod-2, mod)
for i in range(MAXN-2, -1, -1):
	ifac[i] = (i+1)*ifac[i+1]
	ifac[i] %= mod

def C(n, r):
	if n < 0 or r < 0 or r > n:
		return 0
	return (fac[n] * ifac[r] * ifac[n-r])%mod

n=int(input())
if n<13:
    print(0) 
else:
    if (n-13)%2==0:
        avail=(n-13)//2
    else:
        avail=(n-14)//2
    ans=C(avail+6,6)
    print(ans) 