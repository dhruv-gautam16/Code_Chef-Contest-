t=int(input())
for i in range(t):
    w,s=map(str,input().split())
    l=["mon","tues","wed","thurs","fri","sat","sun"]
    a=[]
    b=[]
    d=l.index(s)
    for j in range(int(w)):
        a+=[l[d]]
        if d==6:
            d=0 
        else:
            d+=1 
    for j in l:
        b+=[a.count(j)]
    print(*b)