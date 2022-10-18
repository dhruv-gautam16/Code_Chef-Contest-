# cook your dish here
t= int(input())
for i in range(t):
    n= int(input())
    b=list(map(int,input().split(" ")))
    one = b.count(1)
    if one %2 ==0:
        print("Yes")
    else:
        print("NO")