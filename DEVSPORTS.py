# cook your dish here
for i in range(int(input())):
    z,y,a,b,c = map(int,input().split())
    if (z - y) >= (a + b + c):
        print('YES')
    else:
        print('NO')