for i in range(int(input())):
    a,b=map(int,input().split())
    print('yes') if(abs(a-b)%2==0) else print('no')