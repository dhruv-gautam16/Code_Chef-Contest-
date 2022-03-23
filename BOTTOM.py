x=10
def func(num):
  x=5
  for i in num:
    x*=i 
  return x
print(func((-2,-1,1,2,3)))