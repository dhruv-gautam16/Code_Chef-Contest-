# cook your dish here
import math
for i in range(int(input())):
    x,y=map(int,input().split())
    if x>y:
        print(x-y)
    else:
        print(0)