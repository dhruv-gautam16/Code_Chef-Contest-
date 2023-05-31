
import math
t=int(input())
while t!=0:
    n=int(input())
    if n%10>=5:
        r= math.ceil(n/10)*10
    else:
        r=math.floor(n/10)*10
    print(100-r)
    t-=1
    