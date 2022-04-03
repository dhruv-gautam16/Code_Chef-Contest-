# cook your dish here
for _ in range(int(input())):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    if s//k<=d:print(s//k)
    else:print(d)