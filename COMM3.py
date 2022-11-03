import math

t = int(input())
for _ in range(t):
  n = int(input())
  a, b = map(int,input().split())
  c, d = map(int,input().split())
  e, f = map(int,input().split())
  if math.sqrt((e - a) ** 2 + (f - b) ** 2) <= n:
    print("yes")
  else:
    if math.sqrt((c - a) ** 2 + (d - b) ** 2) <= n and math.sqrt((e - c) ** 2 + (f - d) ** 2) <= n:
      print("yes")
    else:
      print("no")
               