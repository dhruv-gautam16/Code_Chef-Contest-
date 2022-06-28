def bfs(source, adj):
    visited = set()
    visited.add(source)
    
    queue = []
    queue.append((source, 0))
    s = 0
    
    while queue:
        curr, dist = queue.pop(0)
        for node in adj[curr]:
            if node not in visited:
                visited.add(node)
                queue.append((node, dist+1))
                s += dist+1
                
    return s

for _ in range(int(input())):
    n = int(input())
    friends = {}
    for i in range(1, n+1):
        friends[i] = tuple(map(int, input().split()))
        
        # print(friends)
    distance = []
    for i in range(1, n+1):
        distance.append(bfs(i, friends))
        
    # print(distance)
    most_popular = distance.index(min(distance))+1
    
    f = min(distance)/n
    
    average = round(f,6)
    
    print(most_popular, "{:.6f}".format(f))
        