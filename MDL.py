# cook your dish here
from statistics import median
for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    while len(A)!=2:
        med = median(A[:3])
        A.remove(med)
    print(*A)
    