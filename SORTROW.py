T = int(input())
A = []
for i in range(T):
    A.append(list(map(int,input().split(' '))))
dp = [0]*T
for i in range(T):
    for j in range(T):
        dp[j] = A[i][j]
    dp.sort()
    for i in dp:
        print(i , end=' ')
    print(end='\n')