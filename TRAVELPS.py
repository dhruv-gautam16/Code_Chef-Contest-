# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    s=input()
    dummy=0
    for i in s:
        if int(i)==0:
            dummy+=a
        else:
            dummy+=b
    print(dummy)