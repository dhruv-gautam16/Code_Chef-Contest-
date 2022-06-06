t=int(input())
for _ in range(t):
    
    l,r=map(int,input().split())
    if l%2==0:
        print(l," ",l+1," ",l+2," ",l+3)
    elif l+4<=r:
        print(l+1," ",l+2," ",l+3," ",l+4)
    else:
        print("-1")
        

       
    
           
          
        