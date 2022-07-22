# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    ae=[]
    ao=[]
    for i in a:
        if i%2==0:
            ae.append(i)
        else:
            ao.append(i)
    be=[]
    bo=[]
    for i in b:
        if i%2==0:
            be.append(i)
        else:
            bo.append(i)
    ae.sort(reverse=True)
    ao.sort(reverse=True)
    be.sort(reverse=True)
    bo.sort(reverse=True) 
    p=min(len(ae), len(be))
    p1=min(len(ao), len(bo))
    ae1=ae[:p]
    be1=be[:p]
    ao1=ao[:p1]
    bo1=bo[:p1]
    se=(sum(ae1)+sum(be1)+sum(ao1)+sum(bo1))//2 
    ae2=ae[p:]
    be2=be[p:]
    ao2=ao[p1:]
    bo2=bo[p1:] 
    if len(ae2)==0:
        c=be2 
    else:
        c=ae2 
    if len(ao2)==0:
        d=bo2 
    else:
        d=ao2 
    so=0
    for i in range(len(d)):
        so+=(c[i]+d[i])//2 
    print(se+so)
    
     