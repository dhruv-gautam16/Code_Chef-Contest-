a,b=map(int,input().split())
arr=list(map(int,input().split()))
c,d=min(arr),max(arr)
for i in range(b):
    e=int(input())
    if e>=c and e<=d:
        print("Yes")
    else:
        print("No")