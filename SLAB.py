t=int(input())

for _ in range(t):
    total=int(input())
    temp=250000
    tax=0
    slab_per=0.05
    if(total<=temp):
        tax=0
    else:
        for i in range(6):
            taxable=temp+250000
            if(temp==1500000):
                tax+=(slab_per*(total-temp))
                break
            if(total>taxable):
                
                tax+=(slab_per*(taxable-temp))
                temp+=250000
                slab_per+=0.05
                
            else:
                
                tax+=(slab_per*(total-temp))
                break
    tax=int(tax)
    print(total-tax)# cook your dish here
