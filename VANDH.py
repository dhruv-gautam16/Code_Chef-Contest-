# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    ons=0
    zrs=0
    diff=0
    if n>m:
        ons=n
        zrs=n+1
        diff=n-m-1
        strng='0'
        for i in range(n):
            if m+1>0:
                m-=1
                strng+='10'
            else:
                strng+='010'

        print(len(strng),strng,sep="\n")

    elif m>n:
        zrs=m
        ons=m+1
        diff=m-n-1
        strng='1'
        for i in range(m):
            if n+1>0:
                n-=1
                strng+='01'
            else:
                strng+='101'
        print(len(strng),strng,sep="\n")
    elif m==n:
        zrs=m+1
        ons=n+1
        strng='01'
        for i in range(n):
            strng+='01'
        print(len(strng),strng,sep="\n")
        
