for _ in range (int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    maxi = max(arr)
    arr.sort()
    arr.pop()
    print((sum(arr) - (n-1)) + maxi)