# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for j in l:
        if j in d.keys():
            d[j] += 1 
        else:
            d[j] = 1  
    ans = 0
    for k in d.keys():
        ans += min(k - 1, d[k])
    print(ans)    