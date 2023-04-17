# cook your dish here
t=int(input())
for i in range(t):
        X,Y=map(int,input().split())
        if ((Y/X)*100>=50):
                print("YES")
        else:
                print("NO")