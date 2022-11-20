for _ in range(int(input())):
  n,x = map(int,input().split())
  l = list(map(int,input().split()))
  s = sum(l)
  a = s//x
  b = (s-min(l))//x
  if a==b:
    print(-1)
  else:
    print(a)