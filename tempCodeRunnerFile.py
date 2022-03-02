for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=[]
    sum=0
    for i in range(n):
        sum+=a[i]
        d[i]=sum
    int sum1=sum
    for j in range(n):
        sum1=min(sum1,max(d[j],sum-d[j]))
    print(sum1)


