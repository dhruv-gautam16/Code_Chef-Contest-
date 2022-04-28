# cook your dish here
T=int(input())
for i in range (T):
    l=list(map(int,input().split()))
    S=l[0]
    l.remove(S)
    f=0
    r=0
    if sum(l)<=S:
        f+=1
    elif (l[0]+l[1])<=S:
        f+=2
    else:
        f+=3
    l.reverse()
    if sum(l)<=S:
        r+=1
    elif (l[0]+l[1])<=S:
        r+=2
    else:
        r+=3
    print(min(f,r))