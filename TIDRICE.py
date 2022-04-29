# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    d = dict()
    points = 0
    for x in range(n):
        y = list(input().split())
        d[y[0]] = y[1]
    for i in d:
        if d.get(i) == '-':
            points -= 1
        elif d.get(i) == '+':
            points += 1
    print(points)
            