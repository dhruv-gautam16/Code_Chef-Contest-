from itertools import accumulate
for _ in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    flag=0
    
    for i in range(n-1):
        if b[i]%b[i+1]!=0:
            flag=1
            
            
    if flag==1:
        print(-1)
    
    else:
        print(*b)
    