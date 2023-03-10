# cook your dish here
#tst = int(input)

tst = int(input())
for i in range (0,tst):
    x, y = map(int, input().split())
    if (x+y)<=6:
        print("NO")
    else:
        print("YES")