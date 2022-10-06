t=int(input())

while t:
    n=int(input())
    l=list(map(int,input().split(' ')))
    a=[]
    b=[]
    start=l[0]
    i=0
    while i<n:
        if start<l[i]:
            j=i 
            while j<n:
                b.append(l[j])
                j=j+1
            i=j 
            break
        
        else:
            a.append(l[i])
            
        i=i+1 
    if len(a)>0 and len(b)>0:
        print(len(a))
        for x in a:
            print(x,end=" ")
        print("\n")
        print(len(b))
        for y in b:
            print(y,end=" ")
        print("\n")
    else:
        print(-1)
    t=t-1