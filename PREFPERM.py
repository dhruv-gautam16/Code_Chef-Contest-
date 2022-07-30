for _ in range(int(input())):
    n, k = map(int, input().split())
    indices = sorted(map(int, input().split()))
    indices.insert(0, 0)
    for i in range(k):
        for i in range(indices[i+1], indices[i], -1):
            print(i, end=' ')
    print()