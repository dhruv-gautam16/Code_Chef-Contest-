
t=int(input())
for i in range(t):
    k=int(input())
    s=1
    c=0
    while s<=k:
        if s%2!=0:
            c=c+3
        else:
            c=c-1
        s=s+1
    print(c)
            
        
