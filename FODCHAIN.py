t=int(input())
while(t>0):
    e,k=map(int,input().split())
    count=1
    while(e!=0):
        e=e//k
        count=count+1
    
    print(count-1)
    t=t-1
        