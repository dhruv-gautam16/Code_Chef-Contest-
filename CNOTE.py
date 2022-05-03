t = int(input())
for i in range(t):
    x,y,k,n = map(int,input().split())
    count = 0
    for book in range(n):
        p,c = map(int,input().split()) 
        if (p>=(x-y)) and (k>=c):
            count +=1
    if count>=1:        
        print("LuckyChef")
    else:
        print("UnluckyChef")