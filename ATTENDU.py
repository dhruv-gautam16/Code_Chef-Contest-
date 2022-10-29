# cook your dish here
for _ in range(int(input())):
    N=int(input())
    L=input()
    c=0
    for i in L:
        if i=='1':
            c=c+1
        
    days=(120-N)+c
    
    Present=(days*100)/120
   
    if Present>=75:
        print("YES")
    else:
        print("NO")