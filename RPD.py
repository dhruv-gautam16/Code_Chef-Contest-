t=int(input())
for i in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  l=[]
  for j in range(n):
    for k in range(j+1,n):
      z=(a[j]*a[k])
      s=str(z)
      sum=0
      for p in s:
        sum=sum+int(p)
        l.append(sum)
  print(max(l))
        
            
