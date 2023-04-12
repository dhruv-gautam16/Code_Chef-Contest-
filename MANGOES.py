# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print(int((z-y)/x))