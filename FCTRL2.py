def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
for i in range(n):
    num=int(input())
    print(factorial(num))