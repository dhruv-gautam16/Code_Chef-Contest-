# cook your dish here
for _ in range(int(input())):
    n,w,wr = map(int,input().split())
    a = list(map(int,input().split()))
    if wr>=w:
        print("YES")
    else:
        d = {}
        for x in a:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        s=0
        for x in d.keys():
            if d[x]>=2:
                s+=x*(d[x]//2)*2
        if s+wr>=w:
            print("YES")
        else:
            print("NO")