# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    ans = max((arr[-2] * arr[-1]) + (arr[-1] - arr[-2]),(arr[0] * arr[1]) + (arr[1] - arr[0]))
    print(ans)