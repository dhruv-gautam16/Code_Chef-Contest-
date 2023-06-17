for i in range(int(input())):
  N,X,Y = map(int,input().split())
  if (N+1)* Y >=X:
    print("YES")
  else:
    print("NO")