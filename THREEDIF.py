# cook your dish here
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    l.sort()
    m=(10**9)+7
    p=l[0]%m
    q=(l[1]-1)%m
    r=(l[2]-2)%m
    s=(p*q*r)%m
    if l[0]==1 and l[1]==1:
        print(0)
    else:
        print(s)