# cook your dish here
for _ in range(int(input())):
    b,c = map(int,input().split())
    if b%c==0:
        print(1)
    else:
        import math
        t = math.lcm(b,c)//b
        print(t)