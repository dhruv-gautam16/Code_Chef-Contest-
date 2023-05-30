# cook your dish here
t=int(input())
while t>0:
    ls=list(map(int,input().split()))
    a=max(ls)
    ls.remove(max(ls))
    b=sum(ls)
    if(a>b):
        print("YES")
    else:
        print("NO")
    t-=1