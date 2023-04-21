# cook your dish here
t=int(input())
for i in range(t):
        x,a,b=map(int,input().split())
        print("Qualify") if (a+2*b>=x) else print("Notqualify")