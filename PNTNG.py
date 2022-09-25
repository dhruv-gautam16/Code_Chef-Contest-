n,m,h=list(map(int,input().split(' ')))
w=[0]*h
summ=0
for i in range(0,h):
    t,c=list(map(int,input().split()))
    w[i]=[t,c]
    summ=summ+t
w.sort(key=lambda x:x[1])
req=n*m
cost=0
if summ<req:
    print('Impossible')
else:
    
    for e in w:
        if e[0]>req:
            cost=cost+req*e[1]
            req=0
            break
        else:
            cost=cost+e[0]*e[1]
            req=req-e[0]
            
    print(cost)