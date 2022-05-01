for i in range(int(input())):
    a=int(input())
    b=input()
    c=b[:a-1]
    if b[-1] not in c:
        print("NO")
    else:
        print("YES")
    