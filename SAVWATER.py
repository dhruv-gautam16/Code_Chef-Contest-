# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split(" "))
    e=b+c//2
    if(a*e<=d):
        print("YES")
    else:
        print("NO")
