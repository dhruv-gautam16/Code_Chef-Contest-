# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if(a>b):
        print("YES")
    else:
        print("NO")