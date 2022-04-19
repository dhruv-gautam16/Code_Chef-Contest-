for _ in range(int(input())):
    n,d = map(int,input().split())
    l = list(map(int,input().split()))
    r =[]
    nr = []
    for i in l:
        if i>=80:
            r.append(i)
        elif 9>=i:
            r.append(i)
        else:
            nr.append(i)
    if len(r)==0:
        d1 = 0
    elif d>=len(r):
        d1 = 1
    else:
        if len(r)%d==0:
            d1 = len(r)//d
        else:
            d1 = len(r)//d +1
    if len(nr)==0:
        d2 = 0
    elif d>=len(nr):
        d2 = 1
    else:
        if len(nr)%d==0:
            d2 = len(nr)//d
        else:
            d2 = len(nr)//d + 1
    print(d1 + d2)