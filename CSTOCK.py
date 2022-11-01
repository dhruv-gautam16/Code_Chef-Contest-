t = int(input())

while t:
    s,a,b,c=list(map(int,input().split()))[:4]
    
    price = s + ((s*c)/100)
    
    if price >= a and price <= b:
        print("Yes")
    else:
        print("No")
        
    t = t - 1