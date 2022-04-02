
for i in range(int(input())):
    
    a,b,c=map(int,input().split())
    
    sum=a+min(b,c)+int((b-min(b,c))/3)+int((c-min(b,c))/3)
    
    print(sum)
    
