def gcd(a,b):
     
    # Everything divides 0
    if (b == 0):
         return a
    return gcd(b, a%b)
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    while(True):
        g = gcd(a,b)
        if g==1:
            break
        b = b//g
    if b>1:
        print("No")
    else:
        print("Yes")
    
    