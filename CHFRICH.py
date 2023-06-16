# cook your dish here
t = int(input())
for i in range(t):
    a,b,x = map(int,input().split())

    print((b-a)//x)