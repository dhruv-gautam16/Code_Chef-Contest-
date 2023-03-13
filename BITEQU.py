# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n>3:
        print("1 2 3 "+str(3^n))
    elif n==1:
        print("1 4 3 2")
    elif n==2:
        print("2 4 3 1")
    elif n==3:
        print("4 3 1 2")
    else:
        print("4 6 1 5")