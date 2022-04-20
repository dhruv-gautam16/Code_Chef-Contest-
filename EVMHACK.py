for i in range(int(input())):
    a,b,c,p,q,r=map(int,input().split())
    f=(p+q+r)/2
    if(p+b+c>f or a+q+c>f or a+b+r>f):
        print("YES")
    else:
        print("NO")