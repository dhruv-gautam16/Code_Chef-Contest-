t=int(input())
for i in range(t):
    r,g,b=map(int,input().split()) 
    k=int(input()) 
    print(min(r,k-1)+min(g,k-1)+min(b,k-1)+1)