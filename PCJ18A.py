for M in range(int(input())):
    n,x=map(int,input().split(" "))
    a=list(map(int,input().split(" ")))
    if max(a)>=x:
        print('YES')
    else:
        print('NO')# cook your dish here
