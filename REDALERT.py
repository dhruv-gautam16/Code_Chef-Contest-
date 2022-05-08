for j in range(int(input())):
    n,d,h=map(int,input().split())
    a=list(map(int,input().split()))
    sum=0
    al=0
    for i in range(len(a)):
        if(a[i]>0):
            sum+=a[i]
        if(a[i]==0):
            if(sum>d):
                sum-=d
            else:
                sum=0
        if(sum>h):
            al=1
    if(al==1):
        print('YES')
    else:
        print('NO')