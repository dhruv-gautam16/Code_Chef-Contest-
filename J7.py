for jj in range(int(input())):
    p,s=map(int,input().split())
    h=(p-(p*p-24*s)**0.5)/12
    v=h*((s/2)-(h*(p/4 - h)))
    print('%.2f'%v)