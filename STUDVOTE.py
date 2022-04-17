from collections import Counter
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=Counter(l)
    a=[]
    for j in range(n):
        if l[j]==(j+1):
            a+=[j+1]
    count=0
    for j in c:
        if c[j]>=k and j not in a:
            count+=1
    print(count)