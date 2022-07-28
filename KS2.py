def T(n):
    a=[]
    b=str(n)
    for i in b:
        a.append(int(i))
    return sum(a)
a=int(input())
for i in range(a):
    N=int(input())
    b=T(N)
    c=b%10
    s=str(N)
    if c==0:
        e=s+"0"
    else:
        d=10-c
        e=s+str(d)
    print(e)
