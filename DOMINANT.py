# cook your dish here
T = int(input())
for i in range(T):
    a,b,c = map(int, input().split())
    if (a>b+c or b> a+c or c>a+b):
        print("yes")
    else:
        print("no")
    