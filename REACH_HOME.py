motor = int(input())
for f in range(motor):
  F,H =map(int,input().split())
  if (5*F)>=H:
    print("yes")
  else:
    print("no")