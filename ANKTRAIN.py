# cook your dish here
T=int(input())
for i in range(T):
    n=int(input())
    if n==1 or n%8==1:
        print(str(n+3)+"LB")
    elif n==2 or n%8==2:
        print(str(n+3)+"MB")
    elif n==3 or n%8==3:
        print(str(n+3)+"UB")
    elif n==4 or n%8==4:
        print(str(n-3)+"LB")
    elif n==5 or n%8==5:
        print(str(n-3)+"MB")
    elif n==6 or n%8==6:
        print(str(n-3)+"UB")
    elif n==7 or n%8==7:
        print(str(n+1)+"SU")
    else:
        print(str(n-1)+"SL")