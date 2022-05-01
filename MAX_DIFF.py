# cook your dish here
for _ in range(int(input())):
    n,y=map(int,input().split())
    if(n>y):
        print(y)
    else:
        x=y-n
        print(n-x)