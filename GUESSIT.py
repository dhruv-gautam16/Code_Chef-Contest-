t=int(input())

while(t>0):
    t-=1 
    for i in range(1,1000):
        print(i*i)
        x=int(input())
        if(x==1):
            break
    