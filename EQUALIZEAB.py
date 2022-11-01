# cook your dish here
t=int(input())
while(t>0):
    a,b,c=map(int,input().split())
    if(abs(a-b)%(c*2)==0):
        print('YES')
    else:
        print('NO')
    t=t-1