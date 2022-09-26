# cook your dish here

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    a = list(map(int, input().split()))
    l = 8
    m = 0
    for j in range(n - l + 1):
        d = 0
        x = 0
        o = 0 
        for k in range(l):
            c = j + k
            if s[c] == 'd':
                o += 2 * a[k]
            elif s[c] == 't':
                o += 3 * a[k]
            else:
                o += a[k]
            if s[c] == 'D':
                d += 1
            if s[c] == 'T':
                x += 1
        o *= (2 ** d) * (3 ** x) 
        if m < o:
            m = o
    print(m)