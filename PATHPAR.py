# cook your dish here
for _ in range(int(input())):
    N, K = map(int, input().split())
    if N % 2 == 0:
        print("YES")
    elif N & 1 and K & 1:
        print("YES")
    else:
        print("NO")