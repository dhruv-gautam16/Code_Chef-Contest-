# cook your dish here
t=int(input())
while t>0:
    a=list(map(int,input().split(' ')))
    d=(a[0]+a[1])//a[2]
    if d%2==0:
        print("Chef")
    else:
        print("Paja")

    t-=1            
