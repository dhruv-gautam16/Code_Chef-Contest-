# cook your dish here
N = int(input())
T = []
for i in range(N):
    arr = list(map(int, input().split()))
    T.append(arr)
        
for i in range(N):
    for j in range(N):
        for k in range(N):
            T[j][k] = min(T[j][k], T[j][i]+T[i][k])

M = int(input())
for _ in range(M):
    S, G, D = list(map(int, input().split()))
    print(T[S][G]+T[G][D], T[S][G]+T[G][D]-T[S][D])

