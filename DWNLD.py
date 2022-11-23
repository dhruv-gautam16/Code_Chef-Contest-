for tc in range(int(input())):
    n,k=map(int,input().split(" "))
    s=0
    tot=0
    for t1 in range(n):
        tn,dn=map(int,input().split(" "))
        t2=k
        if(k>0):
            k=k-tn
        if(t2>=tn):
            tn=0
        if(k<0):
            tn=-1*k
            k=0
        s=s+(tn*dn)
    print(s)