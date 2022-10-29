for _ in range(int(input())):
  n = int(input())
  l = list(map(int,input().split()))
  a = l.index(1)
  b = n-1-l.index(n)
  if l.index(1) < l.index(n):
    print(a+b)
  else:
    print(a+b-1)