import math
for i in range(int(input())):
    x,y,k=map(int,input().split())
    print(math.ceil(abs(x-y)/k))