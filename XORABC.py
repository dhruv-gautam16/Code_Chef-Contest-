t=int(input())
for i in range (t):
    x= int(input())
    if( (x&1) or (x&(x-1))==0):
        print(-1)
    else:
        print(x//2,0,(x&(x-1))//2)
        