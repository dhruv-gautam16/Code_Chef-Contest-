# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        print(0)
    else:
        ans = pow(2, (n - 1), 1000000007)
        print((ans - 2) % 1000000007)