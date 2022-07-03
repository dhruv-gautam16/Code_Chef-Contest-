# cook your dish here
for _ in range(int(input())):
    x,y=list(input().split())
    x=int(x)
    y=int(y)
    a=list(map(int,input().strip()))
    
    tot=0
    nap=0
    for i in range(len(a)):
        if a[i]==0:
            tot +=1
            
        if a[i]==1:
            nap +=(tot//y)
            
            tot=0
        if a[i]==0 and i==len(a)-1:
            nap +=(tot//y)
    print(nap)