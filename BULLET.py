
for i in range(int(input())):
    x,y,z = map(int,input().split())
    bt = y//x
    ans = z-bt
    if ans < 0:
        ans = 0
    print(ans)