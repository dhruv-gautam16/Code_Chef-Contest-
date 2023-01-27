# cook your dish here
t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = list(input())
    x = s.count("1")
    y = s.count("0")
    f = n // k
    if y % f != 0:
        print("IMPOSSIBLE")
        continue
    z = y // f
    ans1 = z * ("0") + (k - z) * ("1")
    ans = ""
    for j in range(f):
        if j % 2 == 0:
            ans += ans1
            continue
        ans += ans1[::-1]
    print(ans)   