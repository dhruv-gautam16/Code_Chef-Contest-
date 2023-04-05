# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    x=a-c
    y=b-d
    if(x<y):
        print('first')
    elif(x>y):
        print('second')
    else:
        print('any')