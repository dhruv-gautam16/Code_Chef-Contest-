# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    count = 0
    for i in arr:
        if i%2 == 1:
            count += 1
    ans = count//2
    print(ans)