goals = int(input())
for distractions in range(goals):
    aim = int(input())
    wife = list(map(int, input().split()))
    life = list(map(int, input().split()))
    c, e, d = 0, 0, 0
    for death in range(aim):
        if life[death] * wife[death] > c:
            c = life[death] * wife[death]
            e = life[death]
            d = death + 1
        elif life[death] * wife[death] == c:
            if life[death] > e:
                d = death + 1
                e = life[death]
    print(d)