# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split(" "))
    a=str(input())
    s=0
    for i in range(n):
        s=s+(int)(a[i])
    p=s*m
    if(p%2==1):
        print(0)
        continue
    if(s==0):
        print(n*m)
        continue
    a=a
    k,f=0,0
    if(m%2==0):
        for i in range(n):
            if(a[i]=='0'):
                k=k+1
            else:
                break
        for i in range(n-1,0,-1):
            if(a[i]=='0'):
                k=k+1
            else:
                break
        print(k+1)
    else:
        k=0
        s=s//2
        for i in range(n):
            if(k>s):
                break
            elif(k==s):
                f=f+1
                k=k+(int)(a[i])
            elif(k<s):
                k=k+(int)(a[i])
        print(f)