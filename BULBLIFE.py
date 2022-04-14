T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(len(A)):
        sumA = sum(A)
        left = N*X - sumA
    if left>0:
        print(left)
    else:
        print("0")