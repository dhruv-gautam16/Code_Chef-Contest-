from collections import Counter
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=dict(Counter(l))
    m=max(d.values())
    s=sum(d.values())
    rem=s-m
    if(rem==0):
        print(0)
    elif(m>1):
        print(rem+1)
    else:
        print(-1)