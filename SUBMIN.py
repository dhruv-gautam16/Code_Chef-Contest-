t=int(input())
a=list(map(int,input().split()))
q=int(input())
for i in range(q):
    n=int(input())
    count=0
    for j in range(t):
        c=[]
        for k in range(j,t):
            c.append(a[k])
            if(min(c)==n):
                count+=1
    print(count)
        