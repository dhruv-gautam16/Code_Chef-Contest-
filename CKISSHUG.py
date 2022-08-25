modulo=1000000007

def pw2(n):
    if n==0:
        return 1
    r=pw2(int(n/2))
    r=(r*r)%modulo
    if n%2!=0:
        r=(2*r)%modulo
    return r

def solve(n):
    n1=int(n/2)
    n2=n-n1
    return (pw2(n1)+pw2(n2)-2)%modulo

t=int(input())
while t>0:
    n=int(input())
    print(solve(n+1)%modulo)
    t-=1
