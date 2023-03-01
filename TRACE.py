for i in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    t=0
    for i in range(n):
        r,s=0,0
        for j in range(n-i):
            r+=a[j][i+j]
            s+=a[i+j][j]
        t=max(r,s,t)
    print(t)
 