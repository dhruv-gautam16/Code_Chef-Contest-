import math

for jj in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    
    gc=math.gcd(l[0],l[1])
    
    for i in range(2,n):
        gc=math.gcd(gc,l[i])
    print(gc)