# cook your dish 
def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    r=a[0]
    for i in range(1,n):
        r=gcd(r,a[i])
    if(r==1):
        print(0)
    else:
        print(-1)
    