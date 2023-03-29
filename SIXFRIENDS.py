# cook your dish here
t=int(input())
for t in range(t):
    x,y=map(int,input().split())
    if(x*3>=y*2):
        print(y*2)
    else:
        print(x*3)