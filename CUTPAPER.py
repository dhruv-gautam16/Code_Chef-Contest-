cut=int(input())
for c in range(cut):
  n,k=map(int,input().split())
  square=((n//k)**2)
  print(square)