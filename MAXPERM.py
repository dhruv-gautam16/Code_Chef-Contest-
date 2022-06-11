t = int(input())
while t:
    n = int(input())
    arr = [int(i) for i in input().split()]
    d = {}
    for val in arr:
        d[val]=d.get(val,0)+1
    #print(d)
    ans = 0
    for key,value in d.items():
        if key>n:
            ans+=value
        else:
            ans+=(value-1)
    print(ans)
    t-=1