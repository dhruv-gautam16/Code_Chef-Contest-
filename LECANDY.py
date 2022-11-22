# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    if sum(arr)<=b:
        print("Yes")
    else:
        print("No")