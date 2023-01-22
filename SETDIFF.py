# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[-1] - A[0]
    val = 1
    for i in range(len(A) - 2, -1, -1):
        ans += (A[i]*(val + 1)) % 1000000007
        ans -= (A[-i - 1]*(val + 1)) % 1000000007
        val = (2 * val + 1) % 1000000007
    print(ans % 1000000007)