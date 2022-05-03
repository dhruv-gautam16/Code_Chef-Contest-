# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    sum=a[0]
    for i in range(n-1):
        if(a[i+1]>=a[i]):
            sum+=a[i+1]-a[i]
    print(sum)
            
            
