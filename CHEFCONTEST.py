# cook your dish here
for i in range(int(input())):
  X,Y,P,Q = map(int,input().split())
  c1 = X + P*10
  c2 = Y + Q*10
  if c1 < c2:
    print("Chef")
  elif c1 > c2:
    print("Chefina")
  else:
    print("Draw")