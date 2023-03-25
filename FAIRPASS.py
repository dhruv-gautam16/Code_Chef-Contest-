# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n>=k:
        print("NO")
    else:
        print("YES")