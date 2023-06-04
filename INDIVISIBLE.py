for t in range(int(input())):
    a, b, c = map(int, input().split())
    for k in range(1, 100):
        if a%k != 0 and b%k != 0 and c%k != 0:
            print(k)
            break