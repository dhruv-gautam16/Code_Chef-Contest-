for _ in range(int(input())):
    d={}
    for i in range(int(input())):
        k,v = input().split()
        v =int(v)
        if k not in d.keys():
            d[k]=[0,0]
            d[k][v]=1
        else:
            d[k][v]+=1
    s=0
    for j in d.keys():
        s += max(d[j])
    print(s)