n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
s=[ ]
for i in range(0,n):
    if(a[i]>=0):
        c*=1 
    else:
        if(i==n-1):
            a[i]=a[i]*(-1)
            c+=1
            s.append(n)
        else:
            a[i]=a[i]*(-1)
            a[i+1]=a[i+1]*(-1)
            c+=1
            s.append(i+1)
print(c)
for i in s:
    print(i)
        
    
