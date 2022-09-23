for _ in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    f=sorted(list(map(int,input().split())))
    
    
    
    dp=[[n+1 for _  in range(1001)] for _  in range(n)]
    for i in range(n):
        dp[i][0]=0
    for i in range(f[0],1001,f[0]):
        dp[0][i]=i//f[0]
    for i in range(1,n):
        for j in range(1,1001):
            if j>=f[i]:
                dp[i][j]=min(1+dp[i][j-f[i]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    tot=0        
    for i in range(n):
        tot+=dp[n-1][2*h[i]]
    print(tot)
                
    