import sys
from array import array

input = lambda: sys.stdin.buffer.readline().decode().strip()
out=[]

for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[array('b',[int(x) for x in input()]) for _ in range(n)]
    
    if not any([a[i][j] for i in range(n) for j in range(m)]):
        out.extend([' '.join(['-1']*m) for _ in range(n)])
    else:
        row,col=array('b',[0]*n),array('b',[0]*m)
        for i in range(n):
            for j in range(m):
                row[i]|=a[i][j]
                col[j]|=a[i][j]
        
        for i in range(n):
            for j in range(m):
                if a[i][j]==1:
                    a[i][j]=0
                elif row[i] or col[j]:
                    a[i][j]=1
                else:
                    a[i][j]=2
        out.extend([' '.join(map(str,x)) for x in a])            
                
print('\n'.join(out))        