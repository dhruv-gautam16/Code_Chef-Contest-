# cook your dish here
p=int(input())
for i in range(p):
    n=int(input())
    c,m=0,0
    for i in range(n):
        a,b=map(int,input().split())
        a=sum(list(map(int,str(a))))
        b=sum(list(map(int,str(b))))
        if a>b:
            c+=1
        elif a==b:
            c+=1; m+=1
        else:
            m+=1
    if c>m:
        print("0",c)
    elif c<m:
        print("1",m)
    else:
        print("2",c)
    