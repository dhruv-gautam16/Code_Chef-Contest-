# cook your dish here
t=int(input())
while t!=0:
  n=int(input())
  l=list(map(int,input().split()))
  lp=0
  r=0
  j=0
  while j<n:
    if l.index(l[j])==j:
        c=l.count(l[j])
        if c>r:
           r=c
           lp=l[j]
        elif c==r:
           r=c 
           lp=0
    j+=1 
  if lp==0:
        print("CONFUSED")
  else:
        print(lp)
  t-=1