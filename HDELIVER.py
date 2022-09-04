# cook your dish here
def find(node):
    res = node
    while res != par[res]:
        par[res] = par[par[res]]
        res = par[res]
    return res


def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return 0
    if rank[p2] > rank[p1]:
        par[p1] = p2
        rank[p2] += rank[p1]
    else:
        par[p2] = p1
        rank[p1] += rank[p2]
    return 1

t = int(input())
for _ in range(t):
    n, m = list(map(int,input().split()))
    par = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int,input().split()))
        union(a, b)
    q = int(input())
    for _ in range(q):
        x, y = list(map(int,input().split()))
        if find(x) == find(y):
            print('YO')
        else:
            print('NO')