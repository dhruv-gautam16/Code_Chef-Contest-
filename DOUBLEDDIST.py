for i in range(int(input())):
    n=int(input())
    a = sorted(list(map(int, input().split())))
    flag = 1
    for i in range(1, n - 1):
        if a[i] - a[i - 1] == 2 * (a[i + 1] - a[i]) or 2 * (a[i] - a[i - 1]) == a[i + 1] - a[i]:
            flag = 1
        else:
            flag = 0
            break
    if flag:
        print("Yes")
    else:
        print("No")