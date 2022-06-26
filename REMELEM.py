t=int(input())
for q in range(0,t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    l=list(int(i) for i in input().split())
    w=0
    d=len(l)
    l.sort()
    while(d):
        if(d==1):
            break
        a=l[0]
        b=l[1]
        if(a+b <=k):
            l.remove(b)
            d=d-1
        else:
            print("NO")
            w=1
            break
    if(w==0):
        print("YES")