
import math

t = int(input())
for i in range(t):
  n,k= map(int,input().split(' '))
  print(math.comb(n-1,k-1))
