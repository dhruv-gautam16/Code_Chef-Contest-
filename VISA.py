# cook your dish here
for i in range(int(input())):
    x1,x2,y1,y2,z1,z2 = map(int, input().split())
    if x2>=x1:
        if y2>=y1:
            if z2<=z1:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print('NO')