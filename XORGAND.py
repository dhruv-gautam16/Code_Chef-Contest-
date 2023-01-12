# cook your dish here
# cook your dish here
import math as mt

test_case=int(input())

for test in range(test_case): 
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    p = {}
    for i in range(32): p[i] = 0 
    count = [p]
    for j in range(n):
        temp= count[j].copy()
        if a[j] != 0: 
            highestBit = int(mt.log2(a[j]))+1 
        else: 
            highestBit = 0 
        temp[highestBit]+=1 
        count.append(temp)
    for _ in range(q): 
        L,R,X = map(int,input().split())
        if X!=0: 
            xd = int(mt.log2(X))+1 
        else: 
            xd = 0
        print(R-L+1-(count[R][xd]-count[L-1][xd]))
        