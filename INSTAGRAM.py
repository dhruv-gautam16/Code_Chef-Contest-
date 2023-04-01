# cook your dish here
for t in range(int(input())):
    x,y=map(int,input().split())
    if x>y*10:
        print("YES")
    else:
        print("NO")