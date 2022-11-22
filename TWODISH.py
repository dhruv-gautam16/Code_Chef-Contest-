# cook your dish here
for i in range(int(input())):
    n,a,b,c=map(int,input().split())
    if a+c>=n and b>=n:
        print("YES")
    else:
        print("NO")