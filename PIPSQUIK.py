# cook your dish here
t=int(input())
for j in range(t):
    n,h,y1,y2,l=map(int,input().split())
    count=0
    a=[0]*n
    b=[0]*n
    for k in range(n):
        a[k],b[k]=map(int,input().split())
    for i in range(n):
        if(a[i]==1):
            if(h-y1<=b[i]):
                count+=1
            elif(l>1):
                l=l-1
                count+=1
            else:
                break
        if(a[i]==2):
            if(y2>=b[i]):
                count+=1
            elif(l>1):
                l=l-1
                count+=1
            else:
                break
    print(count)
     
                
                    
       
        
    