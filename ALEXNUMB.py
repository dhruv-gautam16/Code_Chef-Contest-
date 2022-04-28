t = int(input())
for x in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    print(n*(n-1)//2)