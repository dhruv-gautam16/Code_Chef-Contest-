
T=int(input())
for i in range(T):
  a,b = map(int,input().split())
  if (a*b)%2==0:
      print("Yes")
  else:
      print("No")