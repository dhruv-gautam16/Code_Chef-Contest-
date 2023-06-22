
t = int(input())
for i in range(t):
  a = list(map(int,input().split(' ')))
  count = 0
  count1 = 0
  for j in range(len(a)):
    if j%2 == 0:
      if a[j] == 1:
        count+=1
    else:
      if a[j] == 1:
        count1+=1
  if count > count1:
    print(1)    
  elif count == count1:
   print(0) 
  else:
   print(2)