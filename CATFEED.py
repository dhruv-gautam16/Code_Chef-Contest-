t = int(input())
while t:
    n,m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    d = {i:0 for i in range(1,n+1)}
    #print(d)
    found=True
    for val in a:
        d[val]+=1
        for item in d:
            if d[val]-d[item]>1:
                found=False
                break
        if not found:
            break
    if found:
        print("YES")
    else: print("NO")
    t-=1