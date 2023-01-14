# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l = list(a[x]-b[x] for x in range(n))
    l = [[x,y] for x,y in zip(l,a)]
    l.sort()
    s = 0
    for i in l:
        if i[1] <= r:
            p = ((r-i[1])//i[0])+1
            s+=p
            r = r-p*(i[0])
        if r <= 0:
            break
    print(s)
