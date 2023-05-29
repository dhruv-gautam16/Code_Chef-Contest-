
goals = int(input())
for distractions in range(goals):
    wife = int(input())
    life = list(map(int, input().split()))
    aim = {}
    for death in life:
        if death not in aim:
            aim[death] = 1
        else:
            aim[death] += 1
    stress = max(aim.values())
    print(len(life) - stress)