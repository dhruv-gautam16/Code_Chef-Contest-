# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x*2 > y*5:
        print("CHOCOLATE")
    elif x*2<y*5:
        print("CANDY")
    else:
        print("EITHER")