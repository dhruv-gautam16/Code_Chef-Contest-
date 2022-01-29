t=int(input())
sum=0
for i in range(t):
    (a,b)=map(int,input().split(' '))
    if a>b:
        print(">")
    elif b>a:
        print("<")
    else:
        print("=")