for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    m = [1] * n
    for i in range(1, n):
        if(arr[i-1] <= arr[i]):
            m[i] = m[i-1] + 1
    print(sum(m))