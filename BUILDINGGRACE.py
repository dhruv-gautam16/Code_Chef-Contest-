# cook your dish here
T=int(input())
for i in range(T):
    A,B,X,Y=map(int,input().split())
    if(A/X<B/Y):
         print("Chef")
    elif(A/X>B/Y):
         print("Chefina")
    else:
         print("Both")