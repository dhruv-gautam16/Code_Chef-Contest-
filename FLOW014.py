n = int(input())
for _ in range(n):
  x = input().split()
  x[0] = int(x[0]) 
  x[1] = float(x[1])
  x[2] = int(x[2])
  if x[0]>50 and x[1]<0.7 and x[2]>5600:
    print(10)
  elif x[0]>50 and x[1]<0.7:
    print(9)
  elif x[1]<0.7 and x[2]>5600:
    print(8)
  elif x[0]>50 and x[2]>5600:
    print(7)
  elif x[0]>50 or x[1]<0.7 or x[2]>5600:
    print(6)
  else:
    print(5)
