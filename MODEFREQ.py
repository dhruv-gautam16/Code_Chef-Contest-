from collections import Counter
t = int(input())

for i in range(t) :
    n=int(input())
    a=list(map(int,input().split()))
    d=dict(Counter(a))
    l=list(d.values())
    d2=Counter(l)
    res=[]
    maxVal = -1
    maxCount = -1
    for x in d2.keys():
        if d2[x]>maxCount:
            maxVal=x
            maxCount=d2[x]
    for x in sorted(d2.keys()):
        if d2[x]==maxCount:
            maxVal=x
            break
    print(maxVal)