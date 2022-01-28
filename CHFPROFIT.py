t=int(input())
sum=0
for i in range(t):
    (x,y,z)=map(int,input().split(' '))
    d=x*y
    e=x*z
    pro=abs(d-e)
    print(pro) 