import math
factors = [0 for _ in range(pow(10, 5)+1)]
for i in range(2, pow(10, 5)+1):
    if factors[i] == 0:
        for j in range(i, pow(10, 5)+1, i):
            factors[j] += 1
ans = [[factors[0]] for _ in range(5)]
for i in range(5):
    for j in range(1, pow(10, 5)+1):
        if factors[j] == (i + 1):
            ans[i].append(1)
        else:
            ans[i].append(0)
        ans[i][j] += ans[i][j-1]
T = int(input())
for t in range(T):
    a, b, x = map(int, input().split())
    print(ans[x-1][b] - ans[x-1][a-1])