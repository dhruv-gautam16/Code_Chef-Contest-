import math
T=int(input())
for i in range(T):
  op = int(input())
  sqr_root = int(math.sqrt(op))
  i_don = 1e10
  for i in range(1,sqr_root+1):
      if op%i==0:
          i_don = min(i_don,op//i - i)
  print(i_don)