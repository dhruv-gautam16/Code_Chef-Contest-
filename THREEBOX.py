# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    s=a+b+c 
    if s<=d:
        print(1)
    else:
        if a+b<=d or b+c<=d or c+a<=d:
            print(2)
        else:
            print(3)