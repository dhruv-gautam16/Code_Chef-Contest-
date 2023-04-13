# cook your dish here
t=int(input())
for _ in range(t):
    n,x=map(int,input("").split())
    a=n//x
    b=a//3
    print(b)