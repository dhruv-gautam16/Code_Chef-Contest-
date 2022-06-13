# cook your dish here
import math
t = input()
for c in range(0, int(t)):
    a, b = input().split()
    gcd = []
    count = 0
    inn = 0
    d = 0
    for x in range(0, 1):
        if abs(int(a) - int(b)) == 1:
            count = 1
            break
        if int(a) > int(b):
            d = int(a) - int(b)
            for i in range(1, math.ceil(math.sqrt(d + 1))):
                if d % i == 0:
                    if i * i == d:
                        count += 1
                    else:
                        count += 2
        if int(b) >= int(a):
            d = int(b) - int(a)
            for i in range(1, math.ceil(math.sqrt(d + 1))):
                if d % i == 0:
                    if i * i == d:
                        count += 1
                    else:
                        count += 2
    print(count)