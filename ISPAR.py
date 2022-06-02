# cook your dish here
T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    if (K == 1 and (N&1)) or K == 2:
        print("ODD")
    else:
        print("EVEN")