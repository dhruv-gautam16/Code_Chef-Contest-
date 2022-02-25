n = int(input())

for i in range(n):
    x = int(input())
    speeds = list(map(int, input().split(' ')))
    cars = 1
    curr_speed = speeds[0]
    for j in range(1,x):
        if curr_speed>=speeds[j]:
            cars += 1
            curr_speed = speeds[j]
    print(cars)