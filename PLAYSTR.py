tes = int(input())
for i in range(tes):
    n = int(input())
    s = list(input())
    r = list(input())
    sum_s = 0
    sum_r = 0
    for item in s:
        sum_s += int(item)
    for item in r:
        sum_r += int(item)
    if sum_s == sum_r:
        print("YES")
    else:
        print("NO")
    
