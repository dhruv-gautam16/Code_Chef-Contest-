for _ in range(int(input())):
    x1, y1, x2, y2=map(int, input().split())
    x3, y3, x4, y4=map(int, input().split())
    d=(x2-x1)*(y2-y1) + (x4-x3)*(y4-y3)
    b1=max(x1, x3)
    b2=max(y1, y3)
    b3=min(x2, x4)
    b4=min(y2, y4)
    if b1<b3 and b2<b4:
        d-=(b3-b1)*(b4-b2)
    print(d)