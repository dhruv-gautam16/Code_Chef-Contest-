import math
for _ in range(int(input())):
    n = int(input())
    x = (0.143 * n) ** n
    if x - math.floor(x) < 0.5:
        print(math.floor(x))
    else:
        print(math.floor(x) + 1)
    
            
            