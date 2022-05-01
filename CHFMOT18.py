# cook your dish here
for i in range(int(input())):
    s,n=map(int,input().split())
    c=0
    if s%2!=0:
        s-=1
        c+=1
    while s!=0:
        if s<=n:
            c+=1
            s=0
        else:
            c+=(s//n)
            s=s%n
    print(c)
        