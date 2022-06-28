# cook your dish here
for _ in range(int(input())):
    x=int(input())
    d2=0
    i=0
    sum=0
    while (sum+(x-pow(2,i)))>0:
        sum +=(x-pow(2,i))
        if x-pow(2,i)>0:
            d2 +=1
        i=i+1
    print(i,end=" ")
    print(d2)