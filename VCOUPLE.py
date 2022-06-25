t = int(input())
for _ in range (t):
    n =int(input())
    a = list(map(int,input().split(' ')))
    a.sort()
    b = list(map(int,input().split(' ')))
    b.sort(reverse= True)
    c = []
    for i in range(n):
         x = a[i] + b[i]
         c.append(x)
    print(max(c))



