
t = int(input())

for _ in range(t):
    n, u, d = map(int, input().split())
    hills = list(map(int, input().split()))
    
    parachute_avail = True
    farthest_hill = n
    
    for i in range(1, n):
        diff = hills[i] - hills[i - 1]
        if diff < 0 and abs(diff) > d:
            if parachute_avail:
                parachute_avail = False
                continue
            farthest_hill = i
            break
        elif diff > u:
            farthest_hill = i
            break
    
    print(farthest_hill)
    
    
        