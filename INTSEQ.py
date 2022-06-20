t = int(input())
for _ in range(t):
    k = int(input())
    ans = 0
    while k%2 != 1:
        ans += 1 
        k = k/2
    print(ans)