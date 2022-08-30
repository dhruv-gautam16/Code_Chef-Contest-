T = int(input())
for _ in range(T):
    N, M, Q = map(int, input().split())
    x_count = [0 for i in range(N)]
    y_count = [0 for j in range(M)]
    for _ in range(Q):
        x, y = input().split()
        x_count[int(x)-1] += 1
        y_count[int(y)-1] += 1
    x_count_odd = 0
    x_count_eve = 0
    y_count_odd = 0
    y_count_eve = 0
    for i in range(N):
        if x_count[i] % 2 == 1:
            x_count_odd += 1
        else:
            x_count_eve += 1
    for j in range(M):
        if y_count[j] % 2 == 1:
            y_count_odd += 1
        else:
            y_count_eve += 1
    print(x_count_odd*y_count_eve + x_count_eve*y_count_odd)