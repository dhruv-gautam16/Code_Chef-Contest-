for _ in range(int(input())):
    n = int(input())
    q = []
    a = list(map(int,input().split(" ")))
    k = []
    l = []
    p =  []
    sum = 0
    reverse = 0
    for i in range(n):
        sum += a[i]
        k.append(sum)
    for i in range(n-1,-1,-1):
        reverse += a[i]
        l.append(reverse)
    l.reverse()
    for i in range(n):
        p.append(k[i] + l[i])
    print(p.index(min(p))+1)
