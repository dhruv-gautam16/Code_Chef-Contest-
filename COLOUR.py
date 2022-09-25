def cal_type_color(x, y, z):
    ans = 0
    if x > 0:
        ans += 1
        x -= 1 
    
    if y > 0:
        ans += 1
        y -= 1 
    
    if z > 0:
        ans += 1
        z -= 1 
    
    if z > 0 and x > 0:
        ans += 1
        x -= 1 
        z -= 1 
    
    if z > 0 and y > 0:
        ans += 1
        y -= 1 
        z -= 1 
    
    if y > 0 and x > 0:
        ans += 1
        y -= 1 
        x -= 1 
    
    return ans


for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    print(cal_type_color(*arr))
