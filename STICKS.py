n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    l.sort()
    l.reverse()
    i=0
    k=[]
    while(i<len(l)-1):
        if(l[i]==l[i+1]):
            k.append(l[i])
            i=i+1
        i=i+1
    s=len(k)
    if(s>1):
        print(k[0]*k[1])
    else:
        print("-1")
    
            
        
        
        
    
    
            
        
        
        
    