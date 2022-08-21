for tc in range(1, int(input()) + 1):
    if tc:
        x, y, k = list(map(int, input().split()))
        b2 = min(x + k, 8)
        b1 = max(x - k, 1)
        h2 = min(y + k, 8)
        h1 = max(y - k, 1)
        length = b2 - b1 + 1
        breadth = h2 - h1 + 1
        print(length * breadth)