t = int(input())
for _ in range(t):
    N, x1,y1,x2,y2 = map(int,input().split())
    cost_internal = abs(x2-x1) + abs(y2-y1)
    cost_external = min((x1-1), (N-x1), (y1-1), (N-y1)) + min((x2-1), (N-x2), (y2-1), (N-y2)) + 2
    print(min(cost_internal, cost_external))