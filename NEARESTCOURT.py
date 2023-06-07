t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    mid = (x+y)//2
    dist1 = abs(mid-x)
    dist2 = abs(mid-y)
    print(max(dist1, dist2))