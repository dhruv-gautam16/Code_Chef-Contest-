from math import gcd
for t in range(int(input())):
    (n,m)=map(int,input().split())
    p=gcd(n,m)
    if p==1:
        print("Yes")
    elif p==n:
        print('No',1)
    else:
        print("No",int(n/p))