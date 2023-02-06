# cook your dish here
# cook your dish here
a= int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    e=list(map(int,input().split()))
    y=0
    for k in range(b):
        if((c-e[k]>d)):
            e[k]=c
            y=y+d
    print(sum(e)-y)