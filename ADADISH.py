t=int(input())
for i in range(t):
    n1=int(input())
    l1=list(map(int,input().split()))
    l1.sort(reverse=True)
    b1=0
    b2=0
    for i in range(n1):
        if b1<b2:
            b1+=l1[i]
        else:
            b2+=l1[i]
    print(max(b1,b2))
