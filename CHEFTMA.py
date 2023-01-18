import heapq
for _ in range(int(input())):
    n, k, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    completed = list(map(int, input().split()))
    white = list(map(int, input().split()))
    black = list(map(int, input().split()))
    
    diff = sorted([tasks[i]-completed[i] for i in range(n)],reverse = True)
    new = white + black
    maxH = [-new[i] for i in range(len(new))]
    heapq.heapify(maxH)
  
    for i,d in enumerate(diff):
        while maxH:
            button = -(heapq.heappop(maxH))
            if d >= button: diff[i] -= button; break
        
    print(sum(diff))
        
    