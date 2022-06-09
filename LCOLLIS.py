# cook your dish here
for i in range(int(input())):
    n,m=map(int,input().split())
    k=[]
    for q in range(n):
        l=list(input())
        k.append(l)
    c=0    
    for w in range(m):
        r=0
        for e in range(n):
            r+=int(k[e][w])
        g=r*(r-1)
        c+=g//2
    print(c)    