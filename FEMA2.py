def compute(mag,iro,k):
    res=0
    while(mag and iro):
        mc=mag.pop()
        ic=iro.pop()
        if mc>ic:
            if (mc-ic)<=k:
                res+=1
            else:
                iro.append(ic)
        else:
            if (ic-mc)<=k:
                res+=1
            else:
                mag.append(mc)
    return res

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    s=s.replace(':','__')
    l=len(s)
    mag=list()
    iro=list()
    ans=0
    for i in range(l):
        if (s[i]=='X'):
            ans+=compute(mag,iro,k)
            mag,iro=[],[]
        elif (s[i]=='I'):
            iro.append(i)
        elif (s[i]=='M'):
            mag.append(i)
    ans+=compute(mag,iro,k)
    print(ans)