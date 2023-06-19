for i in range(int(input())):
    a,b,c,r,x,y,z=map(int,input().split())
    if((x+y+z)>=r and x>=a and y>=b and z>=c):
        print('YES')
    else:
        print('NO')