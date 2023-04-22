import math
for _ in range(int(input())):
    A,B= map(int,input().split())
    LCM = math.lcm(A,B)
    GCD= math.gcd(A,B)
    print(GCD,LCM)
    