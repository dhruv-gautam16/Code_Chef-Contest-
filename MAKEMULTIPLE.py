# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(2*a<=b or a==b):
        print("yes")
    else:
        print("no")