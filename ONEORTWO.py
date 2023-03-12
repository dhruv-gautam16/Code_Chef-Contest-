t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    if a==b:
        if a%2:
            print("CHEF")
        else:
            print("CHEFINA")
    elif a>b:
        d = a - b
        if d==1:
            if a%2:
                print("CHEFINA")
            else:
                print("CHEF")
        else:
            print("CHEF")
    else:
        d = b - a
        if d==1:
            if a%2:
                print("CHEF")
            else:
                print("CHEFINA")
        else:
            print("CHEFINA")