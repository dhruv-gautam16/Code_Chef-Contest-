# cook your dish here
use=int(input())
for u in range(use):
  a,b,c=map(int,input().split())
  if a==c: print(1)
  else:
    if(a-c)%b==0: print((a-c)//b+1)
    else: print((a-c)//b+2)