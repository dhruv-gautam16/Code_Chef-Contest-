
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    max_runs = m * 6 * 6
    if max_runs >= n:
        print("YES")
    else:
        print("NO")
