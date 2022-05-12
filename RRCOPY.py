t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    myset = set()
    for num in arr:
        if num not in myset:
            myset.add(num)

    print(len(myset))