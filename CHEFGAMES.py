# cook your dish here
t=int(input())
for i in range(t):
        R1,R2,R3,R4=map(int,input().split())
        if(R1==0 and R2==0 and R3==0 and R4==0):
                print("IN")
        else:
                print("OUT")
        