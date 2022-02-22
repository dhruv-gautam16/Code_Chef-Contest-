def ans(lst1):
    a = [1] * len(lst1)
    for i in range(len(lst1)-2, -1, -1):
        if lst1[i] * lst1[i+1] < 0:
            a[i] += a[i+1]
    return a
for _ in range(int(input())):
    n = input()
    lst1 = [int(ele) for ele in input().split()]
    print(*ans(lst1))