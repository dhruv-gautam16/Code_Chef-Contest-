ncr=[[0 for i in range (0,1001)] for j in range (0,1001)]
mod=1000000007
def init():
    for i in range (1, 1001):
        ncr[i][1]=i
        ncr[i][i]=1
    for i in range (3,1001):
        for j in range (2,i):
            ncr[i][j]=(ncr[i-1][j-1] + ncr[i-1][j])%mod
init()
t=int(input())
while t>0:
    n=int(input())
    ans=0
    cards=input()
    a=n//2 + 1
    for i in range (a, n+1):
        ans=(ans+ncr[n][i])%mod
    print(ans)
    t-=1