import sys
from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append((v,0))
        self.graph[v].append((u,1))
        
    def ZeroOne(self,source):
        dq=deque()
        dist=[sys.maxsize for i in range(self.V+1)]
        dist[1]=0
        dq.append((source,0))
        while dq:
            node,d=dq.popleft()
            for v,w in self.graph[node]:
                if dist[v]>(w+d):
                    dist[v]=w+d
                    if w==1:
                        dq.append((v,dist[v]))
                    else:
                        dq.appendleft((v,dist[v]))
        return dist[self.V]

n,m=map(int,input().split()) 
g=Graph(n)
for _ in range(m):
    u,v=map(int,input().split())
    g.addEdge(u,v)
ans=g.ZeroOne(1)
if ans==sys.maxsize:
    print(-1)
else:
    print(ans)