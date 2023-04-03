t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    p = x + (x*10)//100
    print(p - (x-y))
