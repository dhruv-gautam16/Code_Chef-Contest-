# cook your dish here
for i in range(int(input())):
  l1 = list(map(str,input().split()))
  l2 = list(map(str,input().split()))
  for i in range(len(l1)):
    if l1[i] in l2:
      print(l1[i])
      break