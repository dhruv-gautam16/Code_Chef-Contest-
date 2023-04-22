t=int(input())
for i in range(t):
        n,x,y=map(int,input().split())
        print("YES") if (y%x==0) else print("NO")