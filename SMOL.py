T=int(input())
for i in range(T):
  n,o = map(int,input().split())
  try:
      print(n%o)
  except:
      print(n)