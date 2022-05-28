T=int(input())
for i in range(T):
  a,n = map(int,input().split())
  try:
      print(str(a//n) +" "+str(a%n))
  except:
      if a==0:
          print("0"+" "+"0")
      elif n==0:
          print("0"+" "+str(a))