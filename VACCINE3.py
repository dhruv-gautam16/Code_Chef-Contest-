# cook your dish here
for _ in range(int(input())):
    N = list(map(int, input().split()))
    G = N[0]
    P = N[1]
    Y = sum(N[G + 1:])
    if G == 10:
        X = 1
    else:
        X = sum(N[G + 2:]) + 1
    print(-(-X//P), -(-Y//P))