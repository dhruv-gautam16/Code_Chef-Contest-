# cook your dish here
for _ in range(int(input())):
    x,y=input().split()
    x=int(x)
    y=int(y)
    if y%2==0:
        if x==1:
            print("even")
        else:
            print("impossible")
    else:
        if x%2==0:
            print("even")
        else:
            print("odd")