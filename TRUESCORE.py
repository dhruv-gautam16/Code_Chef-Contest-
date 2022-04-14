for t in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if c>=a and d>=b:
        print("Possible")
    else:
        print("Impossible")