# cook your dish here
for i in range(int(input())):
    X=int(input())
    if X%4==1:
        print("East")
    elif X%4==2:
        print("South")
    elif X%4==3:
        print("West")
    else:
        print("North")