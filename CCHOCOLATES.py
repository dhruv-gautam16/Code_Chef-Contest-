# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    r=(x*5)+(y*10)
    print(r//z)