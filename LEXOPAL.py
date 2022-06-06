# cook your dish here
n=int(input())
for i in range(n):
    b=list(input())
    a=""
    for i in range(len(b)):
        if(b[i]=='.'):
            if(b[i]==b[len(b)-i-1]):
                b[i]='a'
            else:
                b[i]=b[len(b)-i-1]
    if b==b[::-1]:
        for j in b:
            a=a+str(j)
        print(a)
    else:
        print(-1)