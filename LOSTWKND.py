# cook your dish here
t=int(input())
while(t>0):
    a=list(map(int,input().split()))
    b=[]
    for i in range(0,len(a)-1):
        a[i]=a[i]*a[-1]
        b.append(a[i])
    
    
    total=sum(b)
    if(total>120):
        print("Yes")
    else:
        print("No")
    
    
    
    t=t-1
