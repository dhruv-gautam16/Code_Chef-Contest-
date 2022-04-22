t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    z=100-s
    a=[]
    b=[]
    for j in range(n):
        if l2[j]==0:
            a+=[l1[j]]
        else:
            b+=[l1[j]]
    a.sort()
    b.sort()
    if a==[] or b==[]:
        print("no")
    elif (a[0]+b[0])<=z:
        print("yes")
    else:
        print("no")