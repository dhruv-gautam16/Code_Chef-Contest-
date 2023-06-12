
for _ in range(int(input())):
    x,y=map(int,input().split())
    z=list(map(int,input().split()))
    z.sort()
    print(z[x-y]-1)