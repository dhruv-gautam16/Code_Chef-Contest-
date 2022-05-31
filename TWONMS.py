for i in range(int(input())):
    a,b,n=map(int,input().split())
    if(n%2==1):
        a*=2
    if(a>b):
        print(a//b)
    else:
        print(b//a)