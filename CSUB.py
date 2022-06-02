T=int(input())
for i in range(T):
  n = int(input())
  op = list(input())
  print((op.count("1"))* (op.count("1")+1)//2 )