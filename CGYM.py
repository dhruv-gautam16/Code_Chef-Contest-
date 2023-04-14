# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x+y<=z:
        print("2")
    elif x>z:
        print("0")
    else:
        print("1")