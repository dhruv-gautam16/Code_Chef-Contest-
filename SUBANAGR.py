from collections import Counter
# from heapq import heapify,heappop,heappush
# from math import gcd
#===============================
def solve():
  n=int(input())
  d=(Counter(input()))
  for i in range(n-1):
    d&=(Counter(input()))
  if len(d):
    print(*sorted(d.elements()),sep='')
  else:
    print("no such string")
  
  
  

if __name__=='__main__':

  solve()
    
  

  
