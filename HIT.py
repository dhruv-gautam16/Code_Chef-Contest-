for i in range(int(input())):
    x=int(input())
    l=list(map(int,input().split()))
    n=x//4
    l.sort()
    a=l[n]
    b=l[n*2]
    c=l[n*3]
    if a<b<c and a>max(l[:n]) and b>max(l[n:2*n]) and c>max(l[2*n:3*n]):
        print(a,b,c)
    else:
        print(-1)
