# cook your dish here
flip = int(input())
for f in range(flip):
  n= int(input())
  a= list(map(int,input().split()))
  if n&1==1: print(-1)
  else: print(abs(sum(a))//2)