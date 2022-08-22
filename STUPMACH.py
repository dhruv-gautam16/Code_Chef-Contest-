from heapq import *
def solve():
    #code here
    n = int(input())
    arr = list(map(int,input().split()))
    pq = []
    for i,a in enumerate(arr):
        heappush(pq,[a,i])
    
    j, ans, prev = n, 0, 0
    while j > 0 and pq:
        cur, i = heappop(pq)
        if i < j and cur-prev > 0:
            ans+=(cur-prev)*(j)
            prev = cur
            j = i
    
    return ans
            
for _ in range(int(input())):
    print(solve())