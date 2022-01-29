def factorial(a):
    if a==0:
        return 1
    elif a==1:
        return 1
    else:
        return a * factorial(a-1)
t=int(input())
sum=0
for i in range(t):
    a=int(input())
    print(int(factorial(a)))