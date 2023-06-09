import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    s=2*(x-y)
    print(round(math.sqrt(s)))
    