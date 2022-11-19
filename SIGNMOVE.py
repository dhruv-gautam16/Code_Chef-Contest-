for i in range(int(input())):
    a=int(input())
    if a%2==1:
        print(-(a//2+1))
    else:
        print(a//2)