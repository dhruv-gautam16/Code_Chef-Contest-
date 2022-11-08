# cook your dish here
t=int(input())
while t!=0:
    a,b,k=map(int,input().split())
    if ((a+b)//k)%2==0:
        print("CHEF")
    else:
        print("COOK")
    t-=1 