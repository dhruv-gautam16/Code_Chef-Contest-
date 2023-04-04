t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x!=y and x!=z and y!=z:
        print("YES")
    else:
        print("NO")