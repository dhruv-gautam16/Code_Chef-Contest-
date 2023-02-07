# cook your dish here
# cook your dish here
# find the no. of pairs
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split(' ')))
    l=[]
    for j in range(n):
        for k in range(j+1,n):
            l.append(a[j]+a[k])
    print(l.count(max(l))/len(l))
        