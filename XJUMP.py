
goals = int(input())
for distractions in range(goals):
    life, wife = map(int, input().split())
    print((life % wife) + (life // wife))