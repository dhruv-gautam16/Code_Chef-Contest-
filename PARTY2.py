# cook your dish here
t=int(input())
for t in range(t):
    n,x,k=map(int,input().split())
    if(n*x<=k):
        print("yes")
    else:
        print("no")