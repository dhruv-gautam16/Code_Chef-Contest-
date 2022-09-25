t = int(input())
for _ in range(t):
    n , m = map(int , input().strip().split())
    
    grid = [[0] * m for i in range(n)]
    for i in range(n):
        string = input()
        for j in range(m):
            grid[i][j] = string[j]
    
    marked = [[0] * m for i in range(n)]
    
    for i in range(n-1):
        for j in range(m-1):
            if grid[i][j] == '.' and grid[i+1][j] == '.' and grid[i][j+1] == '.' and grid[i+1][j+1] == '.':
                marked[i][j] = 1 
                marked[i+1][j] = 1 
                marked[i][j+1] = 1 
                marked[i+1][j+1] = 1 
     
    found = False
    for i in range(n):
        for j in range(m):
            if marked[i][j] == 0:
                if grid[i][j] == '.':
                    found = True
                    print('NO')
                    break
        if found:
            break
    else:
        print("YES")
