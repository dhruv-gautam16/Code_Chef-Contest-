from math import*
for n in[*open(0)][1:]:
    n,m=map(int,n.split())
    if m>=2*n:
        a=max((abs(m-m%i-i),i) for i in range(n,2*n))[1]
        print(a,m-m%a)
    else:
        print(n,n)