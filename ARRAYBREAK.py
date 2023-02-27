# cook your dish here
t=int(input())
for i in range(t):
    
    n=int(input())
    count=0
    
    a=list(map(int,input().split()))
    a1=len(a)
    for i in a:
        if i%2==0:
            count=count+1
    if count==a1 or count==0:
        print(0)
        
    else:
        print(count)