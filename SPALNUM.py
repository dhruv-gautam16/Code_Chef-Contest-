def palindrom(j):
     s=str(j)
     s2=s[::-1]
     if s==s2:
          return int(s)
     else:
          return 0
          
for i in range(int(input())):
     sum=0
     a,b=map(int,input().split())
     for j in range(a,b+1):
          sum=sum+palindrom(j)
     print(sum)