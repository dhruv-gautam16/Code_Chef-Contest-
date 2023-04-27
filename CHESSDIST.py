# cook your dish here
for i in range(int(input())):
        x1,y1,x2,y2=map(int,input().split())
        print(max(abs(x1-x2),abs(y1-y2)))