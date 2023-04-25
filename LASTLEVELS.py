t=int(input())
for i in range(t):
    
    x,y,z=map(int,input().split())
    a=x*y
    b=x//3
    if x%3==0:
        b-=1
        print(a+b*z)
    else:
        print(a+b*z)

        

