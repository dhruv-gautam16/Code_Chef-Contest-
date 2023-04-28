import math
for t in range(int(input())):
    x,y=map(int,input().split())
    f1=math.ceil(x/10)
    f2=math.ceil(y/10)
    print(abs(f1-f2))