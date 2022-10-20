for _ in range(int(input())):
    days, eat = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 'YES'
    stored = 0
    for i, bought in enumerate(arr):
        if eat > bought + stored:
            ans = 'NO', i + 1
            break
        else:
            stored += bought - eat
    if ans == 'YES':
        print(ans)
    else:
        print(*ans)