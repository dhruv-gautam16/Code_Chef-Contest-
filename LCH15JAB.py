t = int(input())
for k in range(t):
    a = str(input())
    b = []
    c = set(a)
    for i in c:
        b.append(a.count(i))
    d = max(b)
    if d == len(a)-d:
        print('YES')
    else:
        print('NO')
