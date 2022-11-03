n, q = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for _ in range(q):
  l, r = map(int,input().split())
  s = 0
  for i in range(l, r + 1):
    s += a[i-1]*b[i-1]
  print(s)
    
            
  
