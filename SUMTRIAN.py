# cook your dish here
t=int(input())
for i in range(t):
    l=[]
    m=int(input())
    for j in range(m):
        n=list(map(int,input().split()))
        l.append(n)
    for j in range(m-2,-1,-1):
        for k in range(0, j+1):
            l[j][k]+=max(l[j+1][k],l[j+1][k+1])
    print(l[0][0])