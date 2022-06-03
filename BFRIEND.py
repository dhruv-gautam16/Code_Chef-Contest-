def nearest(l,a,b):
    x=l[0]
    diff=abs(a-x)+abs(b-x)
    for i in l:
        if abs(a-i)+abs(b-i)<diff:
            x=i
            diff=abs(a-i)+abs(b-i)
    return diff
for M in range(int(input())):
    n,a,b,c=map(int,input().split())
    l=list(map(int,input().split()))
    temp=nearest(l,a,b)
    print(temp+c)