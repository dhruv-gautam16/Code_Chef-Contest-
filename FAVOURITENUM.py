fav = int(input())
for f in range(fav):
  num = int(input())
  if num%14==0: print("alice")
  elif num%9==0 and num%2==1: print("bob")
  else: print("charlie")