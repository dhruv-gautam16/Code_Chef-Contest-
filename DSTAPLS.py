T=int(input())
for i in range(T):
  apples,boxes=  map(int,input().split())
  if apples%(boxes**2)==0:
      print("NO")
  else:
      print("YES")