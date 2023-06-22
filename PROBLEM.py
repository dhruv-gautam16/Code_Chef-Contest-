
for _ in range(int(input())):
    n,m=map(int,input().split())
    k=0
    while(m>0 and n>0):
        if m==n:
            k=1
            break
        elif abs(m-n)==1:
            k=0
            break
        elif m>n:
            m=m-1
            n=n+1
        else:
            n=n-1
            m=m+3
    if k==1:
        print("YES")
    else:
        print("NO")