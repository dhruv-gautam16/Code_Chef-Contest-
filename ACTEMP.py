for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a <= b and c <= b:
        print("Yes")
    else:
        print("No")