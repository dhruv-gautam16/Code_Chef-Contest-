# cook your dish here
t=int(input())
for j in range(t):
    n,m,x,y=map(int,input().split())
    if((n-1)%x==0 and (m-1)%y==0):
        print('Chefirnemo')
    elif(n>=2 and m>=2 and (n-2)%x==0 and (m-2)%y==0):
        print('Chefirnemo')
    else:
        print('Pofik')
        
        
    
    