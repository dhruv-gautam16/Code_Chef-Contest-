n,m=map(int,input().split())
a=list(map(int,input().split()))
p=10**9 + 7
for i in range(m):
    x,y=map(int,input().split())
    b=list(map(int,input().split()))
    for j in range(0,2*y,2):
        f1=b[j]*a[x-1]
        f1%=p
        a[b[j+1]-1]+=f1
        a[b[j+1]-1]%=p
    a[x-1]=0
for i in a:
    print(i%p)
            
