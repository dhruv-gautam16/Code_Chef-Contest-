# cook your dish here
for _ in range(int(input())):
    a,b,n=map(int,input().split())
    if n&1==0:
        if a**2>b**2:
            print(1)
        elif a**2<b**2:
            print(2)
        else:
            print(0)
    else:
        if a**3>b**3:
            print(1)
        elif a**3<b**3:
            print(2)
        else:
            print(0)