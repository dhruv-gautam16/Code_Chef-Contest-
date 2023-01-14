# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    s=list(map(int,input().split()))
    maxi, mini = max(s), min(s)
    if mini <= x <= maxi: print("YES")
    else: print("NO")