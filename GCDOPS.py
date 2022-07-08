# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    f=1
    for i in range(n):
        if(a[i]!=i+1):
            if((i+1)%a[i]!=0):
                f=0
    if(f==1):
        print('YES')
    else:
        print('NO')