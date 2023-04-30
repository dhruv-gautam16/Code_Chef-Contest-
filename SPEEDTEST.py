# cook your dish here
t=int(input())
for i in range(0,t):
    x,y,z,a=map(int,input().split())
    sp1=x/y 
    sp2=z/a 
    if(sp1==sp2):
        print("EQUAL")
    elif(sp1>sp2):
        print("ALICE")
    else:
        print("BOB")