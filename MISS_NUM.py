# cook your dish here
T=int(input())
for i in range(T):
    L=list(map(int, input().split()))
    p=max(L)
    L.remove(p)
    s=max(L)
    L.remove(s)
    L1=L
    if sum(L)+s+p==3+s or sum(L)+s+p==2+s: #Conditions for first or both number be 1
        a=1
        b=p-a
        if a<1 or b<1 or a>10**4 or b>10**4:
            print(-1,-1)
            continue
        if a*b==s and min(L1)==a-b:
            L1.remove(min(L1))
            if a//b in L1:
                print(a,b)
                continue
    elif sum(L)+s+p==4*s: #Condition for second number to be 1
        a=1
        b=p-a
        if a<1 or b<1 or a>10**4 or b>10**4:
            print(-1,-1)
            continue
        if a*b==s and min(L1)==b-a:
            L1.remove(min(L1))
            if b//a in L1:
                print(b,a)
                continue
    d=((s**2)-4*p)**0.5 #All other general solutions
    if d in L:
        pass
    elif d*-1 in L:
        d*=-1
    else:
        print(-1,-1)
        continue
    L.remove(d)
    a=(s+d)*0.5
    b=(s-d)*0.5
    if a<1 or b<1 or a>10**4 or b>10**4: # Making sure solution is within constraints
        print(-1,-1)
        continue
    if a//b in L:
        print(int(a),int(b))
    else:
        print(-1,-1)
    