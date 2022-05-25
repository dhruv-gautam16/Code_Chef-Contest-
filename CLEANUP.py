T=int(input())
for i in range(T):
  n,m = map(int,input().split())
  fin = list(map(int,input().split()))
  ty = [int(i) for i in range(1,n+1)]
  #for v in range(1,n+1):
   #   ty.append(v)
  for x in fin:
      ty.pop(ty.index(x))
  chef = []
  other_guy = []
  for s in ty:
      if (ty.index(s)+1)%2==0:
          other_guy.append(s)
      else:
          chef.append(s)
  print(*chef)
  print(*other_guy)