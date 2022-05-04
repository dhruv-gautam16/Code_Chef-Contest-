t=int(input())
for j in range(t):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count=0
    for i in range(n):
        if(b[i]-a[i]==x or b[i]-a[i]==y):
            count+=1
    if(count==n):
        print('Yes')
    else:
        print('No')