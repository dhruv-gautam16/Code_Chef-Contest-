t = int(input())


def getHalf(a, b):
    x = a / 2
    y = b / 2

    return x + y


for _ in range(t):
    n = int(input())
    n_list = list(sorted(map(int, input().split()), reverse=True))

    value = n_list[0]
    for i in range(n - 1):
        value = getHalf(value, n_list[i + 1])

    print(value)
