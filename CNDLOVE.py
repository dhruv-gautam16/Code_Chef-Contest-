t = int(input())
for i in range (t):
  n = int(input())
  l = list(map(int,input().split()))
  s = sum(l)
  if s%2==0:
    print("NO")
  else:
    print("YES")