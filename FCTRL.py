N=int(input())


for i in range(N):
    s=int(input())
    flag=0
    c=5
    while (s/c)>0:
        flag=flag+int(s/c)
        c=c*5
    print(flag)