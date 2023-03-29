t=int(input())
for i in range(t):
     a,b,c,d=map(int,input().split())
     x=a+b
     y=c+d
     if(x<y):
         print(x)
     else:
         print(y)