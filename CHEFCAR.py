n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    n=x-1
    s=(n*(n+1))//2
    a=n-y
    m=0
    if(a!=0 and a>0):
        m=m+y
        q=((a+1)*(a+2))//2
        e=q-1
        m=m+e
        
    else:
        if(a==0):
            m=y
        else:
            m=x-1

    print(s,m)
            
    