# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if(n<=6):
        print(x)
    elif(n%6==0):
        print((n//6)*x)
    else:
        print(((n//6)+1)*x)