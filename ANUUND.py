# cook your dish here
import math
for i in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    lis.sort()
    lis2 = [0]*n
    lis3 = []
    for j in range(math.ceil(n/2)):
        lis2[j*2] = lis[j]
    c = 0
    for j in range(math.ceil(n/2),n):
        lis2[c*2+1] = lis[j] 
        c += 1
    for j in lis2:
        print(j,end=" ")
    print()