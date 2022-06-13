T=int(input())
for i in range(T):
  a,b = map(int,input().split())
  op= a*(a+1 )//2  - b
  if op>=1 and op<=a:
      print(op)
  else:
      print(-1)