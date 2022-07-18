
for _ in range(int(input())):
   r,c = map(int,input().split())
   mat = []
   for _ in range(r):
      st = input()
      mat.append(st)
   ans = 0 
   for i in range(r):
      for j in range(c):
         if i>=2 and i<=r-3 and j>=2 and j<=c-3:
            if mat[i][j]=='^' and mat[i-1][j]=='^' and mat[i-2][j]=='^' and mat[i+1][j]=='^' and mat[i+2][j]=='^' and mat[i][j-1]=='^' and mat[i][j-2]=='^' and mat[i][j+1]=='^' and mat[i][j+2]=='^':
               ans+=1 
   print(ans)