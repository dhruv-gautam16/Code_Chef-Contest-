import math as m
for _ in range(int(input())):
    angels = []
    d = []
    total = 360
    nAngels = int(input())
    angels = list(map(int,input().split()))

    for i in range(1,len(angels)):
        d.append(angels[i]-angels[i-1])
    
    d.append(angels[0]+(360-angels[-1]))
    
    for j in d:
        total = m.gcd(total,j)
    
    print((360//total)-nAngels)