t=int(input())
sum=0
for i in range(t):
    (a,b,c)=map(int,input().split(' '))
    sum=a+b+c 
    if sum==180:
        print("YES")
    else:
        print("NO")