from bisect import bisect_right

def check(n):
    x = bisect_right(arr, n)
    # print(x)
    if arr[x - 1] == n:
        return 0 
    else:
        t = len(arr) - x
        if t % 2 == 0:
            return 1 
        else:
            return -1 

n, q = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
for _ in range(q):
    x = int(input())
    t = check(x)
    if t == 1:
        print('POSITIVE')
    elif t == -1:
        print('NEGATIVE')
    else:
        print(t)
        
    