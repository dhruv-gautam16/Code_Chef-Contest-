# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    plyr = []
    for _ in range(n):
        k = list(map(int, input().split(' ')))
        val = len(k[1:])
        p = {}
        for i in k[1:]:
            p.setdefault(i, 0)
            x = p[i]
            p[i] = x + 1
        h = set(p.keys())
        while len(h) > 3:
            if len(h) == 4:
                val += 1
            elif len(h) == 5:
                val += 2
            elif len(h) == 6:
                val += 4
            p = {k1:v1-1 for k1,v1 in p.items() if (v1-1) > 0}
            h = set(p.keys())
        plyr.append(val)
    
    a = max(plyr)
    if plyr.count(a) > 1:
        print('tie')
    elif plyr.index(a) == 0:
        print('chef')
    else:
        print(plyr.index(a) + 1)
        