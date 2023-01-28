# cook your dish here
t = int(input())
for _ in range(t):
    (n,m) = map(int,input().split())
    (x,y) = map(int,input().split())
    (a,b) = map(int,input().split())
    tdist = (n-x)+(m-y)
    pdist = min((n-a)+(m-b),max((n-a),(m-b)))
    if pdist<tdist: print("NO")
    else: print("YES")