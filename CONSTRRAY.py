# cook your dish here
def solve():
    n = int(input())
    if n & 1:
        print("-1")
        return
    for i in range((n - 1) // 2):
        print("2 -2 ", end="")
    print("2 1")

t = int(input())
for _ in range(t):
    solve()
