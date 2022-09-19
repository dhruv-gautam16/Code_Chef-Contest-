t = int(input())
for _ in range(t):
    nos,noc = map(int,input().split())
    h = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    s = []
    f = [0]*(noc+1)
    for i in range(nos):
        while(s and s[-1][0]<=h[i]):
            f[s[-1][1]] -= 1
            s.pop()
        s.append([h[i],c[i]])
        f[c[i]] += 1
        # print(s)
    # print(s,f)
    ans = 0
    for i in f:
        if i>0:
            ans+=1
    print(ans)
    