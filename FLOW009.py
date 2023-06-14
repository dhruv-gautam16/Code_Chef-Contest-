# cook your dish here
for i in range(int(input())):
    quanity,price=map(int,input().split())
    total = quanity * price 
    if quanity < 1000:
        print(quanity*price)
    else:
        print((quanity*price)-(quanity*price*0.1))