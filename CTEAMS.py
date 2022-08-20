# cook your dish here
from heapq import *
n=int(input())
young=[]
old=[]
c=0
d={}
for i in range(1,n+1):
    a,r=map(int,input().split())
    try:
        d[a].append(r)
    except:
        d[a]=[r]
    if i%2==1: 
        if len(old)==0 or a<old[0]:
            heappush(young,-a)
            c+=r
            
        else:
            heappush(old,a)
            x=heappop(old)
            c+=2*d[x][0]
            c-=r
            heappush(young,-x)
            
    else:
        
        if a>=-young[0]:
            c-=r
            heappush(old,a)
        else:
            x=-heappop(young)
            heappush(young,-a)
            c+=r
            c-=2*d[x][0]
            heappush(old,x)
    print(abs(c))
            
            
        
        