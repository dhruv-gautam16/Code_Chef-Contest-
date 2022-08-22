# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    s = 0
    v = True
    c = 0
    for j in b:
        if j > 100:
            v = False
        if j > 0:
            c += 1
    s = sum(b)
    print('YES' if v and (s - 100 >= 0) and (s - 100 < c) else 'NO')