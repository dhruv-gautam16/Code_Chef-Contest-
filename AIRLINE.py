for i in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    m=0
    n=0
    o=0
    if a+b<=d and c<=e:
        print("YES")
    elif b+c<=d and a<=e:
        print("YES")
    elif a+c<=d and b<=e:
        print("YES")
    else:
        print("NO")
    
