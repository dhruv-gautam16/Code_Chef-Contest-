# cook your dish here
for _ in range(int(input())):
    s=list(map(int,input().split()))
    t1=sum(s[:3])
    t2=sum(s[3:])
    if t1>t2:
        print('1')
    else:
        print('2')