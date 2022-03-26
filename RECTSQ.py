def gcd(a,b):
    if b>a:
        return gcd(b,a)
    if b==0:
        return a
    else:
        return gcd(b,a%b)
for i in range(int(input())):
    x,y = map(int,input().split())
    a = gcd(x,y)
    s = ((x//a) * (y//a))
    print(s)