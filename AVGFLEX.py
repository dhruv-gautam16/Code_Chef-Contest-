import sys
import os 
import math
import collections

# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        x,y = 0,0
        for j in range(N):
            if A[j] <= A[i]:
                x += 1
            elif A[j] > A[i]:
                y += 1
        if x > y:
            ans += 1
    print(ans)