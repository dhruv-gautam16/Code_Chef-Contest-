# cook your dish here
for _ in range(int(input())):
    x, y, k, n = map(int, input().split())
    if abs(y - x) % (2 * k) == 0:
        print('Yes')
    else:
        print('No')