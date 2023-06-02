# cook your dish here
for _ in range(int(input())):
    X,Y= map(int,input().split())
    if (Y-X)%2==0:
        print("Janmansh")
    else:
        print("Jay")