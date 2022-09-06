# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    ali=[int(a) for a in input()]
    fs=ali[0]
    ck=k
    cn=fs
    for a in ali:
        if a!=cn:
            cn=a
            ck-=1
    if ck>0:
        print(-1)
    else:
        ali.reverse()
        zs=0
        ons=0
        hon=False
        hz=False
        if ali.__contains__(0):
            hz=True
            zs=n-ali.index(0)
        if ali.__contains__(1):
            hon=True
            ons=n-ali.index(1)
        ans=0
        if fs==0 and k%2==1:
            ans=ons
        elif fs==1 and k%2==0:
            ans=ons
        elif fs==1 and k%2==1:
            ans=zs
        elif fs==0 and k%2==0:
            ans=zs
        
        if hon and hz:
            print(ans)
        else:
            print(-1)
        