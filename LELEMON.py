# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    l = [int(i) for i in input().split()]
    arr = []
    for i in range(n):
        arr.append([int(i) for i in input().split()][1:])
    for i in arr:
        i.sort()
    ans = 0
    for i in l:
        if arr[i] == []:
            continue
        else:
            ans += arr[i].pop()
    print(ans)