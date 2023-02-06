# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    max_like=0
    max_comment=0
    ans=0
    for i in range(n):
        if a[i]>max_like:
            max_like=a[i]
            max_comment=b[i]
            ans=(i+1)
            
        elif a[i]==max_like and b[i]>max_comment:
            max_like=a[i]
            max_comment=b[i]
            ans=(i+1)
            
    print(ans)
            