# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    maxNum = 0
    count = 0
    for i in range(n):
        if arr[i] > maxNum:
            maxNum = arr[i]
            count += 1
    print(count)