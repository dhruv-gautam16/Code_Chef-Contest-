
t = int(input())

for _ in range(t):
    gf = input().split(":")
    bf = input().split(":")
    dist=int(input())
    time1 = int(gf[0])*60 + int(gf[1])
    time2 = int(bf[0])*60 + int(bf[1])
    waited = abs(time1-time2)
    print(float(waited+dist),end=" ")
    if((dist*2)<waited):
        print(float(waited))
    else:
        print(dist+(waited)/2)
