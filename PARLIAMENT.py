parli = int(input())
for p in range(parli):
  n,x = map(int,input().split())
  print('yes') if 2*x>=n else print("no")