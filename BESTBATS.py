from itertools import combinations
t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    k=int(input())
    x.sort(reverse=True)
    w=sum(x[:k])
    u=list(combinations(x,k))
    count=0
    for j in u:
        if(sum(j)==w):
            count+=1
    
    print(count)
