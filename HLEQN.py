import math
for _ in range(int(input())):
    x = int(input())
    flag = 0
    for b in range(1,math.ceil(math.sqrt(x))):
        a = (x-2*b)/(b+2)
        if a-math.floor(a) == 0 and a>0:
            #print(a,b)
            flag = 1
    if flag == 1:
        print("YES")
    else:
        print("NO")