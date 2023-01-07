# cook your dish here
goals = int(input())
for i in range(goals):
    aim = int(input())
    wife, Life, knife = 0, 0, 0
    life = list(map(int, input().split()))
    for death in life:
        wife += (death == 0)
        Life += (death == 1)
        temp = min(wife, Life)
        wife -= temp
        Life -= temp
        knife += temp
    print(knife + Life // 3)