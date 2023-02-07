# cook your dish here
# cook your dish here
# cook your dish here
for _ in range(int(input())):

  a = input()

  chk = "frieza"
  res = ''
  y = 0
  n = 0
  temp_n=[]
  temp_y=[]
  for i in a:
    if i in chk:
      if len(temp_n) != 0:
        res = res + str(max(temp_n))
        n = 0
        y += 1
        temp_y.append(y)
        temp_n=[]
      else:
        n = 0
        y += 1 
        temp_y.append(y)
        temp_n=[]
    else:
      if len(temp_y) != 0:
        res = res + str(max(temp_y))
        y = 0
        n += 1
        temp_n.append(n)
        temp_y=[]
      else:
        y = 0
        n += 1
        temp_n.append(n)
        temp_y=[]
  if len(temp_y) != 0:
    res = res + str(max(temp_y))
  if len(temp_n) != 0:
    res = res + str(max(temp_n))
  print(res)