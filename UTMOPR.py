for _ in range(int(input())):
  x,y = map(int,input().split())
  z = list(map(int,input().split()))
  if sum(z)%2==0 and y==1:
    print("odd")
  else:
    print("even")