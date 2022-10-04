# cook your dish here
t = int(input())
for u in range(t):
    length,k = map(int , input().split())
    arr = list(map(int , input().split()))
    if k > length:
        print (max(arr))
    else:
        dp = [-1000000000 for i in range(length)]
        for i in range(length):
            if i - k >= 0:
                dp[i] = max(0,dp[i-k]) + arr[i]
            else:
                dp[i] = arr[i]
        ans = -100000000
        for i in range(1,k+1):
            ans = max(ans,dp[-i])
        print (ans)
