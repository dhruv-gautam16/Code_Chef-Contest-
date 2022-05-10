# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    w=0
    p=a[0]
    q=b[0]
    if(p==q):
        w+=p
    for i in range(1,len(a)):
        p+=a[i]
        q+=b[i]
        if(a[i]==b[i] and p==q):
            w+=a[i]
    print(w)
        