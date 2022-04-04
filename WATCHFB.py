for i in range(int(input())):
    n=int(input())
    c=a=b=0
    for i in range(n):
        r,x,y=map(int,input().split())
        if r==1 or x==y:
            c=1
            a=x
            b=y
            print("YES")
        else:
            g=max(a,b)
            h=min(x,y)
            if h<g and c==1:
                print("YES")
                if a>b:
                    a=max(x,y)
                    b=min(x,y)
                else:
                    a=min(x,y)
                    b=max(x,y)
            else:
                print("NO")