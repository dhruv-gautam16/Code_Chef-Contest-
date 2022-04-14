# cook your dish here
a=int(input())
b=int(input())
ar=a*b 
per=(2*(a+b))
if per>ar:
    print("Peri")
    print(per)
elif ar>per:
    print("Area")
    print(ar)
elif ar==per:
    print("Eq")
    print(ar)