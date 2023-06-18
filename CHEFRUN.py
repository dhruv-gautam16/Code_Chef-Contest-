for i in range(int(input())):
  X1,X2,X3,V1,V2 = map(int,input().split())
  S1 = (X3-X1)/V1
  S2 = (X2-X3)/V2
  if S1 > S2:
    print("Kefa")
  elif S1 < S2:
    print("Chef")
  else:
    print("Draw")