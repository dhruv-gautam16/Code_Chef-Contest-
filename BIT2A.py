goals = int(input())
for distractions in range(goals):
    life = int(input())
    wife = list(map(int, input().split()))
    knife = []
    death = 0
    for i in wife:
        for j in wife:
            if i != j and j > i:
                death += 1
        knife.append(death)
        death = 0
    print(*knife)