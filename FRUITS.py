t=int(input())
while(t): 
    n,m,k=map(int,input().split()) 
    d=abs(n-m) 
    if(d<=k):print(0) 
    else:print(d-k) 
    t-=1