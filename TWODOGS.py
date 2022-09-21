# cook your dish here
# cook your dish here
n,k=map(int,input().split())
A=map(int,input().split())
D,dist={}, {}
for i,a in enumerate(A):
    D[a]=0
    dist[a] = min(dist.get(a, float("inf")), i, n - i - 1)

hk = k / 2
c = float("inf")
for a in D:
    if a < hk:
        b = k - a
        if b in D:
            c = min(c, max(dist[a], dist[b]))
print(-1 if c == float("inf") else c + 1)