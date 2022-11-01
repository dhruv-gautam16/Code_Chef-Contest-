t=int(input())
for i in range(t):
    n,v1,v2=map(int,input().split())
    t1=n*2**0.5/v1
    t2=2*n/v2
    if t1<t2:
        print('Stairs')
    else:
        print('Elevator')
