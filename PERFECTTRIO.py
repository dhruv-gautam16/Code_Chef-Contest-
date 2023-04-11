for t in range(int(input())):
    a,b,c = map(int,input().split())
    if(a==b+c):
        print("YES")
    elif(b==a+c):
        print("YES")
    elif(c==b+a):
        print("YES")
    else:
        print("NO")