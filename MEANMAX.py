for _ in range(int(input())):
    n = int(input())
    l = list(map(int , input().split()))
    k = max(l)
    y = (sum(l)-k)/(n-1)
    print(k+y)
    