# cook your dish here 
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split())) 
    b=list(map(int,input().split()))  
    c=arr+b 
    c.sort() 
    mini=c[-1] 
    for i in range(n+1):
        mini=min(mini,(c[i+n-1]-c[i])) 
    print(mini)
    
    
