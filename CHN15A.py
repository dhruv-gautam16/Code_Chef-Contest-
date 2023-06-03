t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    minions = list(map(int, input().split()))
    count = sum(1 for minion in minions if (minion + k) % 7 == 0)
    print(count)
