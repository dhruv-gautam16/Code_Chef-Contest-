# cook your dish here
T = int(input())
ans = []
for i in range(T):
    N, M = [int(i) for i in input().split()]
    A = []
    for i in range(N):
        x = list(input())
        A.append(x)
    count = 0
    for s in range(2, min(N, M) + 1):
        for i in range(N - s + 1):
            for j in range(M - s + 1):
                if(A[i][j] == A[i + s - 1][j] and A[i][j] == A[i][j + s - 1] and A[i][j] == A[i + s - 1][j + s - 1]):
                    count += 1
    ans.append(count)
for i in ans:
    print(i)