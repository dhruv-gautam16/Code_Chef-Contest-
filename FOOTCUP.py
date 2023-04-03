for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    if(x==0 and y==0):
        print("NO")
    elif(x==y):
        print("YES")
    else:
        print("NO")