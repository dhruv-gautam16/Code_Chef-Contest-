# cook your dish here
def recur(dp, matrix, i, j, n, m):
    if i>=0 and j>=0 and i<n and j<m:
            # print('o')
        if dp[i][j]!=-1:
            return dp[i][j]
        if matrix[i][j] == 'P':
            dp[i][j] =  1+max(recur(dp,matrix,i-1,j+2,n,m),
            recur(dp,matrix,i+1,j+2,n,m),
            recur(dp,matrix,i-2,j+1,n,m),
            recur(dp,matrix,i+2,j+1,n,m))
            
        else:
            dp[i][j] =  max(recur(dp,matrix,i-1,j+2,n,m),
            recur(dp,matrix,i+1,j+2,n,m),
            recur(dp,matrix,i-2,j+1,n,m),
            recur(dp,matrix,i+2,j+1,n,m))
        return dp[i][j]
    else:
        return 0
    
    
for _ in range(int(input())):
    n = int(input())
    board = []
    
    for _ in range(n):
        board.append(list(input()))
        
    dp = [[-1]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                x = i 
                y = j
                break
    print(recur(dp,board,x,y,n,n))
    
        