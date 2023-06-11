for i in range(int(input())):
    a,b=map(int,input().split())
    c=(a/(b**2))
    if c<=18:
        print(1)
    elif c>=30:
        print(4)
    elif c>18 and c<25:
        print(2)
    elif c>24 and c<30:
        print(3)