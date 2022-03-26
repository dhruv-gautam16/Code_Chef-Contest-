for _ in range(int(input())):
    count = 0
    for i in range(10):
        n = list(map(int, input().split()))
        for j in n:
            if j < 31:
                count +=1
    if count >= 60:
        print("yes")
    else:
        print("no")