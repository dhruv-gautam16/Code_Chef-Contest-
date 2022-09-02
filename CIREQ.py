# cook your dish here
import heapq


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr = sorted(arr)
    q = list()
    heapq.heappush(q, 1)
    for i in range(n) :
        if arr[i] >= q[0] :
            heapq.heappush(q, q[0] + 1)
            heapq.heappop(q)
        else :
            heapq.heappush(q, 2)
   
    print(len(q))