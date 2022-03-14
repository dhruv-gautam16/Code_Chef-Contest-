for i in range(int(input())):
    n=int(input())
    s=input()
    modulo=998244353
    l=[0]*n 
    p=1 
    if s[0]=='1':
        l[0]=1 
    x=l[0]
    for i in range(1,n):
        if s[i]=='1':
            x+=i+1 
        l[i]=x 
        l[i]=l[i]%2 
    res=0
    for i in range(n-1,-1,-1):
        if l[i]==1:
            res+=p
            res%=modulo
        p*=2 
    p%=modulo
    print(res%modulo)
        
        