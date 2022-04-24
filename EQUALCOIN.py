for jj in range(int(input())):
    x,y=map(int,input().split())
    
    value=x+y*2
    if value&1==1:
        print('no')
    else:
        if x>0 or y&1==0:
            print('yes')
        else:
            print('no')