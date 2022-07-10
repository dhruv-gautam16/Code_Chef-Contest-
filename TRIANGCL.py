# cook your dish here
# cook your dish here
# cook your dish here
id=int(input())
t=int(input())
for i in range(t):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    d1 = (x1-x2)**2 + (y1-y2)**2
    d2 = (x1-x3)**2 + (y1-y3)**2 
    d3 = (x2-x3)**2 + (y2-y3)**2
    
    angle=""
    length=""
    
    arr=[d1,d2,d3]
    arr.sort()
    
    if arr[2]>arr[0]+arr[1]:
      angle= "obtuse"
    elif arr[2]<arr[0]+arr[1]:
        angle= "acute"
    else:
        angle= "right"
    
    if d1!=d2 and d2!=d3 and d3!=d1:
        length="Scalene"
    else:
        length="Isosceles"  
        
    if id==1:
        print(length + " triangle")
    else:
        print(length + " " + angle + " triangle")
        
