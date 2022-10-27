import math
for _ in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    c=0
    for i in range(n+1):
        for j in range(i):
            if sum(ar[j:i])==math.prod(ar[j:i]):
                c+=1
    print(c)