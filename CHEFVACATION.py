# cook your dish here
for i in range(int(input())):
  X,Y,Z = map(int,input().split())
  if X+Y <= Z:
    print("YES")
  else:
    print("NO")