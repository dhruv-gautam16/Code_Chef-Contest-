# cook your code here
for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        x, y = map(int, input().split())
        ans = ans ^ i 
    print(ans)