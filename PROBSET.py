for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[]
    for i in range(n):
        l=input().split()
        a.append(l)
    s="FINE"
    for i in a:
        c=i[1].count("1")
        if i[0]=="correct":
            if c!=k:
                s="INVALID"
                break
        else:
            if c==k:
                s="WEAK"
    print(s)
