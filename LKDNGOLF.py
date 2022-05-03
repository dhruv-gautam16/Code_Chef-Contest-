t=int(input())
for j in range(t):
    n,x,k=map(int,input().split())
    if(x%k==0 or (n+1-x)%k==0):
        print("YES")
    else:
        print("NO")