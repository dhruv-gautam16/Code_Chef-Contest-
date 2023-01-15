for _ in range(int(input())):
    n=int(input())
    a=[*map(int,input().split())]
    x,y=0,0
    d={}
    for i in a:
        if d.get(i)==None:d[i]=1
        else:d[i]+=1
        if i%2==0:x+=1
        else:y+=1
    res=(x*(x-1))//2+(y*(y-1))//2
    for i in d.keys():
        res-=(d[i]*(d[i]-1))//2
    for i in d.keys():
        if d.get(i)!=None and d.get(i^2)!=None:
            res-=(d[i]*d[i^2])/2
    print(int(res))
    