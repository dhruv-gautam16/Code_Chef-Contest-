distance=lambda x1,y1,x2,y2:(((x2-x1)**2)+((y2-y1)**2)*(0.5))
for i in range(int(input())):
    n=int(input())
    points=[]
    for i in range(n):
        a,b = map(int,input().split())
        points.append([a,b])
    y=None
    for j in range(n-1):
        nk=j+1
        for k in range(j+1,n):
            x=distance(points[j][0],points[j][1],points[k][0],points[k][1])
            if y==None or x<y:
                y=x
                nk=k 
        print(j+1,nk+1)