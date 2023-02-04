# cook your dish here
n=int(input())
for i in range(n):
    s=input()
    l=s.split()
    x=int(l[0])
    y=int(l[1])
    if (x==y*2) :
        print(x//2)
    elif x>y :
        z=x-y
        print(z)
    else :
        print(0)