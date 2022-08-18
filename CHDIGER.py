# cook your dish here
t = int(input())

for i in range(t):
    n, d = input().split()
    s = list(n)
    l = list(n)
    p = d
    k = 0
    for j in range(len(l) - 1, -1, -1):
        if n[j] > p:
            s[j] = ''
            k += 1
        else:
            p = s[j]
    s = ''.join(s) + d * k
    print(s)