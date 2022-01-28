t=int(input())
sum=0
for i in range(t):
    x=int(input())
    for i in range(100):
        a,b,c=i,i+1,i+2
        sum=a+b+c 
        avg=sum/3
        if(avg==x):
            print(a,b,c)
            break
        else:
            continue