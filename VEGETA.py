# cook your dish here


from math import ceil,sqrt

nn = 1000000
l=[0]*(nn+1)
for i in range(2,nn+1):
    if l[i]==0:
        j=1
        while i*j <= nn:
            l[i*j] += 1
            j += 1

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    c = 0
    for i in range(n,m):
        c += l[i]
    print(c)
