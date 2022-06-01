# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for i in range(n):
        l.append((k//a[i])*b[i])
    print(max(l))
