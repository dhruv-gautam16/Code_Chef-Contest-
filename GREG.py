n,m=map(int,input().split())
mi=2
ma=n+m
ans=[1 for i in range(ma+1)]

for i in range(2,int(ma**0.5)+1):
    for j in range(i+i,ma+1,i):
        ans[j]=0
ans[0]=0
ans[1]=0
print(ans.count(1))
    
        
        
