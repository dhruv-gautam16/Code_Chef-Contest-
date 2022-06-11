def cal(x,y):
    if x==0:
        return y
    else:
        return cal(y%x,x)
for i in range(int(input())):
    n,x,y,k=map(int,input().split())
    a,b=n//x,n//y
    z=n//((x*y)//cal(min(x,y),max(x,y)))
    if a+b-2*z>=k:
        print("Win")
    else:
        print("Lose")